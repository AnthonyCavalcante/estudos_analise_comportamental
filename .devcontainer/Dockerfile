FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN pip install --upgrade pip
RUN pip install ipython black flake8

ENV PYTHONUNBUFFERED=1
