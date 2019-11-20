#!/bin/bash
# this script manages uninstallation
# works in three modes:
# --all: delete all dependencies (including python)
# --no-python: delete all dependencies (excluding python)
# --rpg: delete only dependencies connected to libretro

if [[ "$#" -e 0 ]]; then
	./install/install.sh show_warning
elif [[ "$1" == "--all" ]]
	# remove retroarch packages
	sudo apt-get -y purge retroarch-assets
	sudo apt-get -y purge retroarch
	# remove libretro repository
	sudo add-apt-repository --remove -y ppa:libretro/stable
	# remove python dependencies
	head -n -6 ~/.bashrc > tmp
	mv tmp ~/.bashrc 
	rm tmp
elif [[ "$1" == "--no-python" ]]
	# remove retroarch packages
	sudo apt-get -y purge retroarch-assets
	sudo apt-get -y purge retroarch
	# remove libretro repository
	sudo add-apt-repository --remove -y ppa:libretro/stable
elif [[ "$1" == "--rpg" ]]
	# TODO
fi
