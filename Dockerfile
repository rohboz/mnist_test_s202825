# Base image
FROM python:3.9-slim

# install python 
RUN apt update && \
apt install --no-install-recommends -y build-essential gcc && \
apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/
COPY .dvcignore .dvcignore
COPY .dvc/ .dvc/
COPY data.dvc data.dvc
COPY reports/ reports/

WORKDIR /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN dvc config core.no_scm true

ENTRYPOINT dvc pull && python -u src/models/docker_train_test.py