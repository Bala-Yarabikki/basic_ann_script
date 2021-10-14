import tensorflow as tf


def get_data(validation_datasize):
    mnist = tf.keras.datasets.mnist
    (X_train,y_train),(X_test,y_test) = mnist.load_data()

    X_train,x_val  = X_train[:validation_datasize]/255., X_train[validation_datasize:]/255.
    y_train,y_val  = y_train[:validation_datasize]/255., y_train[validation_datasize:]/255.

    X_test = X_test/255.

    return (X_train, y_train), (x_val, y_val),(X_test, y_test)