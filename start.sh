#!/bin/bash
# this script starts up the application
# no parameters - start
# -i - install
if [[ "$#" -eq 0 ]]; then
	echo "Starting Raspberry Pi Gaming Station"
	cd src/rpg-station
	python3 runner.py
fi
if [[ "$#" -ge 1 ]]; then
	if [[ "$1" == "-i" ]]; then
		echo "Starting installation script"
		./install/install.sh
	elif [[ "$1" == "-h" ]]; then
		echo "Start Raspberry Pi Gaming Station - ./start.sh"
		echo "Install all dependencies - ./start.sh -i"
	else
		echo "Wrong parameters"
		echo "Use ./start.sh -h for help"
	fi
fi
