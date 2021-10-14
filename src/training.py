import argparse

import epochs as epochs

from src.utils.common import read_config
from src.utils.data_mgmt import get_data
from src.utils.model import create_model


def training(config_path):
    config = read_config(config_path)
    validation_datasize = config["params"]['validation_datasize']
    (X_train, y_train), (x_val, y_val), (X_test, y_test) = get_data(validation_datasize)

    loss_function = config["params"]["loss_function"]
    metrics = config["params"]["metrics"]
    optimizer = config["params"]["optimizer"]
    num_classes = config["params"]["num_classes"]
    epochs = config["params"]["epochs"]
    model = create_model(loss_function, metrics, optimizer, num_classes)

    validation_set = (x_val, y_val)

    history = model.fit(X_train, y_train,
                        epochs=epochs,
                        validation_data=validation_set)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('--config', "-c", default="config.yaml")

    parsed_args = args.parse_args()

    training(config_path=parsed_args.config)
