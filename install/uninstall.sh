#!/bin/bash
# this script manages uninstallation
# works in three modes:
# --all: delete all dependencies (including python)
# --no-python: delete all dependencies (excluding python)
# --rpg: delete only dependencies connected to libretro

function uninstall_rpg() {
	# check that retroarch installed
	RACHECK=$(flatpak list | grep org.libretro.RetroArch)
	# uninstall retroarch
	if [[ -n "$RACHECK" ]] ; then
	flatpak uninstall -y flathub org.libretro.RetroArch
	fi
	
	# check that libretro-super is downloaded
	LSCHECK=$(ls ~/. | grep libretro-super)
	if [[ -n "$LSCHECK" ]] ; then
		CURRENTPATH=$(pwd)
		cd ~/.
		# remove libretro-super
		sudo rm -r libretro-super
		# remove packages needed to install libretro-super
		sudo apt-get -y purge libxkbcommon-dev zlib1g-dev libfreetype6-dev \
		libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libavcodec-dev \
		libsdl2-dev libsdl-image1.2-dev libxml2-dev yasm
		cd $CURRENTPATH
	fi
}

function uninstall_pyht() {
	# remove python and pip commands default version aliases
	head -n -6 ~/.bashrc > tmp
	mv tmp ~/.bashrc 
	rm tmp
	. ~/.bashrc
	
	# remove python packages
	sudo pip uninstall -r ../requirements.txt

	# remove pip
	sudo apt-get -y purge python3-pip
}

function uninstall_pkgs() {
	# uninstall defualt platforms
	./uninstall_platform.sh nestopia
	./uninstall_platform.sh snes9x
	./uninstall_platform.sh mgba
	./uninstall_platform.sh gambatte
	
	# remove system-prepare packages
	sudo apt-get -y purge software-properties-common build-essential flatpak
}

if [[ "$#" -e 0 ]]; then
	./install/install.sh show_warning
elif [[ "$1" == "--all" ]]
	uninstall_rpg
	uninstall_pyth
	uninstall_pkgs
elif [[ "$1" == "--no-python" ]]
	uninstall_rpg
	uninstall_pkgs
elif [[ "$1" == "--rpg" ]]
	uninstall_rpg
fi

sudo apt-get -y update
