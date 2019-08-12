#!/bin/bash
# this script runs the Python script
# for importing games
# into Raspberry Pi Gaming Station
# no parameters - import directory
# -f - import single file
# -f <filename> - import by filename
function show_warning() {
	echo "Wrong parameters"
	echo "Use ./import.sh -h for help"
}

if [[ "$#" -eq 0 ]]; then
	echo "Pick a directory to import files from"
	cd src/rpg-station
	python3 importer.py
elif [[ "$#" -eq 1 ]]; then
	if [[ "$1" == "-h" ]]; then
		echo "Pick a directory to import to Raspberry Pi Gaming Station - ./import.sh"
		echo "Pick a file to import to Raspberry Pi Gaming Station - ./import.sh -f"
		echo "Import specified file to Raspberry Pi Gaming Station - ./import.sh -f <filename>"
	elif [[ "$1" == "-f" ]]; then
		echo "Pick a file to import"
		cd src/rpg-station
		python3 importer.py -f
	else
		show_warning
	fi
elif [[ "$#" -eq 2 ]]; then
	if [[ "$1" == "-f" ]]; then
		echo "Trying to import file $2 to Raspberry Pi Gaming Station"
		cd src/rpg-station
		python3 importer.py -f $2
	else
		show_warning
	fi
else
	show_warning
fi
