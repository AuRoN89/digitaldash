FROM navikey/raspbian-buster
LABEL version="1.0"
LABEL description="Dockerfile to build DD ISO"

RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install python3-setuptools git-core python3-dev

# Kivy deps
RUN apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev \
   gstreamer1.0-plugins-bad, gstreamer1.0-plugins-base, \
   gstreamer1.0-plugins-good, gstreamer1.0-plugins-ugly \
   gstreamer1.0-omx, gstreamer1.0-alsa, libmtdev-dev \
   xclip xsel libjpeg-dev
RUN apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# INSTALL RUST
RUN curl https://sh.rustup.rs -sSf | sh
RUN rustup override set nightly

# INSTALL OUR REPOs
RUN git clone https://github.com/kaiserengineering/digitaldash

# INSTALL PYTHON DEPS
RUN python3 -m pip install -r digitaldash/requirements.txt

# RUN DOCKER LOCALLY
# docker build --no-cache . |  grep "Successfully built" | sed 's/Successfully built //g' | xargs -I{} docker run {}

# docker build -t "image:Dockerfile" .
# docker run -it image:Dockerfile /bin/bash

# BUILD OUR ISO
