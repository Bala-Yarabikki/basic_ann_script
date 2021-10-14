import tensorflow as tf
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.activations import relu, softmax


def create_model(loss_function,metrics,optimizer,num_classes):
    model = Sequential()
    model.add(Flatten(input_shape=[28, 28], name="inputlayer"))
    model.add(Dense(300, activation=relu))
    model.add(Dense(100, activation=relu))
    model.add(Dense(num_classes, activation=softmax))

    model.summary()

    model.compile(loss=loss_function,
                  optimizer=optimizer,
                  metrics=metrics)

    return model  # untrained model