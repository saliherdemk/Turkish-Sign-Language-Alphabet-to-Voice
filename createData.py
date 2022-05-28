import os
import cv2
import numpy as np
import pickle

DATADIR = "./NewDataset"

CATEGORIES = ["A","B","Bosluk","C","D","E","F","G","H","I","K","L","M","N","Nokta","O","P","R","S","Sil","T","U","V","Y","Z"]

IMG_SIZE = 64

train_data = []

def create_train_data():
    i = 0
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))

                _ ,roi = cv2.threshold(img_array,120,255, cv2.THRESH_BINARY)

                new_array = cv2.resize(roi, (IMG_SIZE, IMG_SIZE))
                train_data.append([new_array,class_num])
            except:
                print("broken")
        i += 1
        print(i , len(CATEGORIES), sep=" / " )
    print(len(train_data))

    np.random.shuffle(train_data)

    X = []
    Y = []

    for features, label in train_data:
        X.append(features)
        Y.append(label)

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    Y = np.array(Y)

    pickle_out = open("Stored/train_X.pickle", "wb")
    pickle.dump(X,pickle_out)
    pickle_out.close()

    pickle_out = open("Stored/train_Y.pickle", "wb")
    pickle.dump(Y,pickle_out)
    pickle_out.close()

    return train_data

if(__name__ == "__main__"):
    create_train_data()