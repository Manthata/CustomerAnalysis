ARG UBUNTU_VERSION=16.04
FROM ubuntu:${UBUNTU_VERSION}

ARG USE_PYTHON_3_NOT_2=True
ARG _PY_SUFFIX=${USE_PYTHON_3_NOT_2:+3}
ARG PYTHON=python${_PY_SUFFIX}
ARG PIP=pip${_PY_SUFFIX}

RUN apt update && apt -y upgrade && apt -y install \
    build-essential \
    cmake \
    git \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    python-dev \
    python-numpy \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libdc1394-22-dev

RUN apt-get update && apt-get install -y \
    ${PYTHON} \
    ${PYTHON}-pip \
    ${PYTHON}-tk

RUN ${PIP} install --upgrade \
    pip \
    setuptools

WORKDIR /app
# WORKDIR /usr/src/app
ADD . /app

# write the necessary libraries in cpu_requirements.txt including opencv-python and opencv-contrib-python
RUN ${PIP} install --trusted-host pypi.python.org -r requirements.txt
# COPY . .


# FROM continuumio/anaconda3.7
#  WORKDIR /usr/src/app
# # RUN conda install -c conda-forge opencv
# COPY requirements.txt ./
# RUN pip3 install --no-cache-dir -r requirements.txt
# COPY . .
CMD [ "python", "camera.py" ]