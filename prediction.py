# https://github.com/Mirwe/Real-time-ASL-alphabet-recognition/blob/main/hand_tracking.py for hand tracking
# https://www.geeksforgeeks.org/python-displaying-real-time-fps-at-which-webcam-video-file-is-processed-using-opencv/ for counting FPS

import cv2
import mediapipe as mp
import tensorflow as tf
import numpy as np
import time
import textwrap
import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Turkish

def speak(text):
  engine.say(text)
  try:
    engine.runAndWait()
  except Exception as ep:
    print(ep)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

test_model = tf.keras.models.load_model("3x128x1-CNN.model")

TEST_CATEGORIES = ["A","B","Bosluk","C","D","E","F","G","H","I","K","L","M","N","Nokta","O","P","R","S","Sil","T","U","V","Y","Z"]

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    prev_frame_time = 0
    new_frame_time = 0

    char = ""
    word = ""
    count_same_text = 0

    while cap.isOpened():
      ret, frame = cap.read()

      frame = cv2.flip(frame, 1)

      old_char = char

      if not ret:
        print("Ignoring empty camera frame.")
        continue

      frame.flags.writeable = False
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      results = hands.process(frame)

      frame.flags.writeable = True
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

      if results.multi_hand_landmarks:
        xList = []
        yList = []
        bbox = []
        lmList = []
        landmarks = results.multi_hand_landmarks

        for hand in landmarks:
          for id, lm in enumerate(hand.landmark):
              h, w, c = frame.shape
              px, py = int(lm.x * w), int(lm.y * h)
              xList.append(px)
              yList.append(py)
              lmList.append([px, py])

          xmin, xmax = min(xList), max(xList)
          ymin, ymax = min(yList), max(yList)
          boxW, boxH = xmax - xmin, ymax - ymin
          bbox = xmin, ymin, boxW, boxH

          roi_x = bbox[0] - 50
          roi_y = bbox[1] - 50
          roi_w = bbox[2] + 100
          roi_h = bbox[3] + 100

        try:
          cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_w, roi_y + roi_h), (255, 255, 0), 2)

          roi = frame[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]

          img = cv2.resize(roi, (64, 64))

          _, fin = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

          prediction = test_model.predict(fin.reshape(1, 64, 64, 3))

          char_index = np.argmax(prediction)

          confidence = round(prediction[0, char_index] * 100, 1)
          predicted_char = TEST_CATEGORIES[char_index]

          char = predicted_char

          if(predicted_char == "Bosluk"):
            char = " "

          if(char == "Nokta"):
            char = "."

          if (old_char ==  char):
            count_same_text += 1
          else:
            count_same_text = 0

          print(count_same_text)
          if(count_same_text > 10):
            old_text = char

            if(char == "Sil"):
              word = word[:-1]
            else:
              word = word + char

            if(char == "."):
              threading.Thread(target=speak, args=(word,)).start()
              word = ""
            count_same_text = 0

          frame = cv2.putText(frame, predicted_char, (roi_x, roi_y - 5),  fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2, color = (0, 0, 0),thickness= 4)
          cv2.imshow("asd",fin)
        except Exception as ep:
          print(ep)

      new_frame_time = time.time()

      fps = 1 / (new_frame_time - prev_frame_time)
      prev_frame_time = new_frame_time

      fps = str(int(fps))

      frame = cv2.putText(frame, "FPS: " + fps, (10, 30), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1,
                          color=(0, 0, 0), thickness=1)

      wrapped_text = textwrap.wrap(word, width=35)

      blackboard = np.zeros((120, 640, 3), dtype=np.uint8)

      # https://stackoverflow.com/questions/56660241/how-to-wrap-text-in-opencv-when-i-print-it-on-an-image-and-it-exceeds-the-frame
      for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, cv2.FONT_HERSHEY_TRIPLEX, 1, 2)[0]

        gap = textsize[1] + 10

        y = int((blackboard.shape[0] + textsize[1]) / 2) + i * gap
        x = int((blackboard.shape[1] - textsize[0]) / 2)

        cv2.putText(blackboard, line, (x, y), cv2.FONT_HERSHEY_TRIPLEX,
                    1,
                    (255, 255, 255),
                    2,
                    lineType=cv2.LINE_AA)

      # progress bar
      for i in range(count_same_text):
        cv2.rectangle(blackboard,(0,10),(80 * i,30),(255,255,255),-1)


      res = np.vstack((frame, blackboard))

      cv2.imshow('TSL Recognizer', res)

      if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
