import os
import cv2
import numpy as np
import pickle
from LETTERS import LETTERS

from pathlib import Path

DATADIR = "NewDataset"

IMG_SIZE = 64

DIRECTORY = Path("Stored")
DIRECTORY.mkdir(parents=True, exist_ok=True)

train_data = []


def create_train_data():
    i = 0
    for category in LETTERS:
        path = os.path.join(DATADIR, category)
        class_num = LETTERS.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))

                _, roi = cv2.threshold(img_array, 120, 255, cv2.THRESH_BINARY)

                new_array = cv2.resize(roi, (IMG_SIZE, IMG_SIZE))
                train_data.append([new_array, class_num])
            except:
                print("broken")
        i += 1
        print(i, len(LETTERS), sep=" / ")
    print(len(train_data))

    np.random.shuffle(train_data)

    X = []
    Y = []

    for features, label in train_data:
        X.append(features)
        Y.append(label)

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    Y = np.array(Y)

    pickle_out = open(os.path.join(DIRECTORY, "train_X.pickle"), "wb")
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open(os.path.join(DIRECTORY, "train_Y.pickle"), "wb")
    pickle.dump(Y, pickle_out)
    pickle_out.close()

    return train_data


if __name__ == "__main__":
    create_train_data()
