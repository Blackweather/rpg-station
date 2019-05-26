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
CHECK=$(dpkg -s retroarch | grep Status)
if [[ $CHECK != "Status: install ok installed" ]]
then 
	sudo apt-get -y install retroarch
fi

CHECK=$(dpkg -s retroarch-assets | grep Status)
if [[ $CHECK != "Status: install ok installed" ]]
then
	sudo apt-get -y install retroarch-assets
fi
