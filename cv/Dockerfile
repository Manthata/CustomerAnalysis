FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y upgrade && apt-get -y install \
    build-essential \
    cmake \
    git \
    libgtk2.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libdc1394-22-dev \
    pkg-config \
    python-dev \
    python-numpy \
    python-tk \
    python3-tk \
    software-properties-common \
    tk-dev \
    zlib1g-dev 

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
ADD . /app

# write the necessary libraries in cpu_requirements.txt including opencv-python and opencv-contrib-python
RUN pip3 install --upgrade && pip3 install --trusted-host pypi.python.org -r requirements.txt

CMD [ "python3", "camera.py" ]