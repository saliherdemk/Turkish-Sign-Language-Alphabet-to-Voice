import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

IMAGES_PATH = "NewDataset"

i = 0

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,) as hands:

    while cap.isOpened():
      success, image = cap.read()

      image = cv2.flip(image, 1)

      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = hands.process(image)

      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      if results.multi_hand_landmarks:
        xList = []
        yList = []
        bbox = []
        lmList = []
        landmarks = results.multi_hand_landmarks

        for hand in landmarks:

          for id, lm in enumerate(hand.landmark):
              h, w, c = image.shape
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
          roi_h = bbox[3] + 100
          roi_w = bbox[2] + 100

        cv2.rectangle(image, (roi_x, roi_y), (roi_x + roi_w, roi_y + roi_h), (255, 0, 0), 2)

        roi = image[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]

        try:
          img = cv2.resize(roi, (64, 64))

          i += 1
          if i % 2 == 0:
              cv2.imwrite(IMAGES_PATH + '/Sil/' + str(8) + str(int(i / 2)) + '.png', roi)

          print(i)
          if cv2.waitKey(1) == ord('q') or i > 400:
            break

        except:
          print("no hands | broken")

      cv2.imshow('MediaPipe Hands', image)
      if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()