import pickle
import time

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard


# Different models were tried and the best model was found with the help of Tensorboard
# https://www.youtube.com/watch?v=BqgTU7_cBnk
def find_optimum_model():

    dense_layers = [0, 1, 2]
    layer_sizes = [32, 64, 128]
    conv_layers = [1, 2, 3]

    pickle_in = open("Stored/train_X.pickle", "rb")
    train_x = pickle.load(pickle_in)

    pickle_in = open("Stored/train_Y.pickle", "rb")
    train_y = pickle.load(pickle_in)

    train_x = train_x / 255.0

    for dense_layer in dense_layers:
        for layer_size in layer_sizes:
            for conv_layer in conv_layers:
                name = "{}-conv-{}-nodes-{}-dense-{}".format(
                    conv_layer, layer_size, dense_layer, int(time.time())
                )
                tensorboard = TensorBoard(
                    log_dir="logs/{}".format(name)
                )  # If you get an error, make sure this path is not include any non-english character

                model = Sequential()

                for _ in range(conv_layer):
                    model.add(
                        Conv2D(
                            filters=layer_size,
                            kernel_size=(3, 3),
                            input_shape=train_x.shape[1:],
                            activation="relu",
                        )
                    )
                    model.add(MaxPooling2D(pool_size=(2, 2)))

                model.add(Flatten())

                for _ in range(dense_layer):
                    model.add(Dense(layer_size, activation="relu"))

                model.add(Dense(25, activation="softmax"))

                model.compile(
                    loss="sparse_categorical_crossentropy",
                    optimizer="adam",
                    metrics=["accuracy"],
                )

                model.fit(
                    train_x,
                    train_y,
                    batch_size=32,
                    epochs=5,
                    validation_split=0.1,
                    callbacks=[tensorboard],
                    shuffle=True,
                )


if __name__ == "__main__":
    find_optimum_model()
