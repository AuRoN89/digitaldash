FROM navikey/raspbian-buster
LABEL version="1.0"
LABEL description="Dockerfile to build DD ISO"

RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install python3-setuptools git-core python3-dev build-essential curl

# Kivy deps
RUN apt-get -y install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
libgstreamer1.0-dev libmtdev-dev xclip xsel libjpeg-dev

RUN apt-get -y install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# INSTALL RUST
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

# INSTALL OUR REPOs
RUN git clone --branch docker https://github.com/kaiserengineering/digitaldash

# COPY CONFIG.txt TO /boot
RUN cp digitaldash/docker/config.txt /boot/

# Change dir so we pickup our rust-toolchain.toml file
WORKDIR "/digitaldash"

# INSTALL PYTHON DEPS
RUN python3 -m pip install -r digitaldash/requirements.txt

# RUN DOCKER LOCALLY
# docker build -t "image:Dockerfile" .
# docker run -it image:Dockerfile /bin/bash

# BUILD OUR ISO
