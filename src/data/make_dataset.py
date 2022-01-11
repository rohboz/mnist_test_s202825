# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import click
import numpy as np
import torch
import torch.utils.data as data_utils
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    images = [
        np.load(input_filepath + "train_%i.npz" % cnt)["images"] for cnt in range(5)
    ]
    images.append(np.load(input_filepath + "test.npz")["images"])
    labels = [
        np.load(input_filepath + "train_%i.npz" % cnt)["labels"] for cnt in range(5)
    ]
    labels.append(np.load(input_filepath + "test.npz")["labels"])
    normalize = lambda X: 0.5 * (X - np.mean(X)) / (np.std(X)) + 0.5
    images = torch.tensor(normalize(np.concatenate(tuple(images))))
    labels = torch.tensor(np.concatenate(labels))
    train_data = data_utils.TensorDataset(images[:25000, :, :], labels[:25000])
    test_data = data_utils.TensorDataset(images[25000:, :, :], labels[25000:])

    torch.save(train_data, output_filepath + "trainset.pt")
    torch.save(test_data, output_filepath + "testset.pt")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
