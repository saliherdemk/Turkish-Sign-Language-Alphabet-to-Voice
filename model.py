import pickle
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

def model_run():
    pickle_in = open("Stored/train_X.pickle", "rb")
    train_x = pickle.load(pickle_in)

    pickle_in = open("Stored/train_Y.pickle", "rb")
    train_y = pickle.load(pickle_in)

    train_x = train_x / 255.0

    model = Sequential()

    model.add(Conv2D(filters=128, kernel_size=(3, 3), input_shape=train_x.shape[1:], activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=128, kernel_size=(3, 3), input_shape=train_x.shape[1:], activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=128, kernel_size=(3, 3), input_shape=train_x.shape[1:], activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(128, activation="relu"))

    model.add(Dense(25, activation="softmax"))

    model.compile(loss="sparse_categorical_crossentropy", optimizer="Adam", metrics=['accuracy'])

    model.fit(train_x, train_y, batch_size=32, epochs=1, validation_split=0.1,shuffle=True)

    model.save('Models/3x128x1-CNN.keras')

if(__name__ == "__main__"):
    model_run()
