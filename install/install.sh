#!/bin/bash
# this script manages initial configuration
# and dependencies

# TODO:
# check if repository already in sources.list

# add repository to source packages
sudo add-apt-repository -y ppa:libretro/stable 
# update source packages
sudo apt-get update

# TODO:
# check if required packages are installed
sudo apt-get -y install retroarch*
