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

WORKDIR /
RUN pip install -r requirements.txt --no-cache-dir

ENTRYPOINT dvc pull && python -u src/models/train_model.py