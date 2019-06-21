#!/bin/bash
# this script manages initial configuration
# and dependencies

#check if python3 is installed
PYCHECK=$(which python3 | echo $?)
if [[ $PYCHECK != "0" ]] ; then
	sudo apt-get install libssl-dev openssl
	wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
	tar xzvf Python-3.5.0.tgz
	cd Python-3.5.0
	./configure
	make
	sudo make install
fi

# TODO:
# check if repository already in sources.list

# add repository to source packages
sudo add-apt-repository -y ppa:libretro/stable 

# check if required packages are installed and update source packages
CHECK=$(dpkg -s retroarch | grep Status)
if [[ $CHECK != "Status: install ok installed" ]] ; then
	sudo apt-get update
	sudo apt-get -y install retroarch
fi

CHECK=$(dpkg -s retroarch-assets | grep Status)
if [[ $CHECK != "Status: install ok installed" ]] ; then
	sudo apt-get update
	sudo apt-get -y install retroarch-assets
fi
