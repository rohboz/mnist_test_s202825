MNIST 02476
==============================


To fulfill the dependencies run: \
-- pip install -r requirements.txt \
To process data raw data run: \
-- python src\\data\\make_dataset.py data\\raw\\corruptmnist data\\processed \
Or access data through from dvc: \
-- dvc pull \
To train model and generate training run png run: \
-- python src\\models\\train_model.py \
To use trained model for prediction run: \
-- python src\\models\\predict_model.py models\\trained_models\\model.pt data\\processed\\testset.pt \
Build dockerimage to run training-pipeline: \
-- docker build -f trainer.dockerfile . -t trainer:latest --no-cache \

  
---
Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── .dvc
    │   ├── plots          <- Data from third party sources.
    │   │   └── ...
    │   ├── .gitignore
    │   └── config
    ├── .dvcignore         <- Ignore file for dvc
    ├── data.dvc           <- Configuration details for dvc
    │
    ├── tests
    │   ├── test_data.py   <- Test data
    │   └── test_model.py  <- Test model
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    ├── .gitignore         <- Ignore file for git
    ├── test_environment.py<- Test for environment setup.
    ├── Dockerfile         <- dockerfile to be activated by gcp trigger at git push
    ├── cloudbuild.yaml    <- Build file for Dockerfile in gcp
    ├── trainer.dockerfile <- Local dockerfile not cloud
    ├── .flake8            <- Configuration file for flake8
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
