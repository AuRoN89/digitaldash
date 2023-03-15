FROM navikey/raspbian-buster
LABEL version="1.0"
LABEL description="Dockerfile to build DD ISO"

ENV CARGO_NET_GIT_FETCH_WITH_CLI=true
ENV PATH="/root/.cargo/bin:$PATH"

ADD docker/config.txt /boot/
ADD docker/dd_gui.service /etc/systemd/system/
ADD docker/dd_webapp.service /etc/systemd/system/

LABEL com.iximiuz-project="docker-to-linux"
RUN apt-get -y update
RUN apt-get -y install --no-install-recommends \
  linux-image-amd64 \
  systemd-sysv
RUN echo "root:root" | chpasswd

RUN DEBIAN_FRONTEND=noninteractive apt-get -y update

RUN apt-get -y install --no-install-recommends \
  linux-image-amd64

RUN apt-get -y install --no-install-recommends \
  systemd-sysv

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
    python3-setuptools git-core python3-dev git\
    wget build-essential curl python3-pip libssl-dev \
    gcc g++ make

# Kivy deps
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
libgstreamer1.0-dev libmtdev-dev xclip xsel libjpeg-dev

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# INSTALL RUST
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y --default-toolchain nightly --profile minimal

# INSTALL OUR REPOs
RUN git clone --branch docker https://github.com/kaiserengineering/digitaldash

# INSTALL STANDALONE PYTHON
RUN wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz
RUN tar -xf Python-3.11.1.tar.xz
WORKDIR "/Python-3.11.1"
RUN ./configure
RUN make altinstall -j `nproc`

WORKDIR "/digitaldash"

# INSTALL PYTHON DEPS
RUN python3.11 -m pip install -r requirements.txt

# Temp install command that will be handled by requirements.txt
RUN python3.11 -m pip install git+https://github.com/craigkai/kivy@initialize-logger

RUN python3.11 /digitaldash/themes/loadThemes.py

WORKDIR "/digitaldash/frontend"

RUN curl -sL https://deb.nodesource.com/setup_19.x | bash -s
RUN apt-get install -y nodejs

RUN npm install --include=dev
RUN npm run build

# RUN DOCKER LOCALLY
# docker build -t "image:Dockerfile" .
# docker run -it image:Dockerfile /bin/bash

# BUILD OUR ISO
