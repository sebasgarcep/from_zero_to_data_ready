FROM ubuntu:20.04

RUN apt update

# Install curl, jq, mdb-tables and mdb-export
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Bogota
RUN apt-get install curl jq mdbtools apt-transport-https ca-certificates gnupg python3-pip libpq-dev -y

# Install gscloud and gsutil
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y

# Create base directory
RUN mkdir /home/pipelines
WORKDIR /home/pipelines

# Create data folder
RUN mkdir data

# Copy Pipfiles
COPY Pipfile .
COPY Pipfile.lock .

# Run pipenv
RUN pip3 install pipenv

# Install dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Read testing
ARG PYTHON_ENV=production
ENV PYTHON_ENV=$PYTHON_ENV

# Copy scripts into docker
COPY main.py .
COPY src/ src/
COPY tests/ tests/
COPY mocks/ mocks/

# Run data pipelines
CMD python3 -m green