# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import click
import numpy as np
import torch
import torch.utils.data as data_utils
from dotenv import find_dotenv, load_dotenv
from torch import nn


@click.command()
@click.argument("modelpath", type=click.Path(exists=True))
@click.argument("datapath", type=click.Path())
def main(modelpath, datapath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    testdata = torch.load(datapath)
    testloader = torch.utils.data.DataLoader(
        testdata, batch_size=len(testdata), shuffle=True
    )

    # Flatten MNIST images into a 784 long vector
    images, labels = next(iter(testloader))
    images = images.view(images.shape[0], -1)
    # TODO: Test pass
    model = nn.Sequential(
        nn.Linear(784, 256),
        nn.ReLU(),
        nn.Dropout(0.25),
        nn.Linear(256, 128),
        nn.ReLU(),
        nn.Dropout(0.25),
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Dropout(0.25),
        nn.Linear(64, 10),
        nn.LogSoftmax(dim=1),
    )
    model.load_state_dict(torch.load(modelpath))
    with torch.no_grad():
        logps = model(images.float())
    ps = torch.argmax(torch.exp(logps), dim=1)
    Trues = torch.eq(ps, labels)

    print(torch.sum(Trues) / len(Trues))


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
