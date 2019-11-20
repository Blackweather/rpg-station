#!/bin/bash
# this script starts up the application
# no parameters - start
# -i - install
function show_warning() {
	echo "Wrong parameters"
	echo "Use ./start.sh -h for help"
}

if [[ "$#" -e 0 ]]; then
	echo "Starting Raspberry Pi Gaming Station"
	cd src/rpg-station
	python3 runner.py
elif [[ "$#" -eq 1 ]]; then
	if [[ "$1" == "-i" ]]; then
		echo "Starting installation script"
		./install/install.sh
	elif [[ "$1" == "-u" ]]; then
		echo "Starting uninstallation script"
		./install/uninstall.sh $2
	elif [[ "$1" == "-h" ]]; then
		echo "Start Raspberry Pi Gaming Station - ./start.sh"
		echo "Install all dependencies - ./start.sh -i"
		echo "Uninstall all dependencies (including python) - ./start.sh -u --all"
	    echo "Uninstall all dependencies (excluding python) - ./start.sh -u --no-python"
		echo "Uninstall only dependencies connected to libretro - ./start.sh -u --rpg"

	else
		show_warning
	fi
else
	show_warning
fi
