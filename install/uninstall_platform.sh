#!/bin/sh
# this script uninstalls the libretro core specified as input parameter
# example usage: ./uninstall_platform.sh nestopia
sudo apt-get -y remove --purge libretro-$1
