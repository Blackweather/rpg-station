#!/bin/sh
# this script installs the libretro core specified as input parameter
# example usage: ./install_platform.sh nestopia
sudo apt-get -y install libretro-$1
