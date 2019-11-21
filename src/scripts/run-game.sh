#!/bin/bash
# this scripts run the specified rom file
# with a specified libretro core
# example usage: ./run-game.sh gambatte ../../rom/gb/adjustris.gb

# TODO: change the path to standard path on raspbian
libretro_path='/usr/lib/arm-linux-gnueabihf/libretro/'
core_extension='_libretro.so'
if [[ $# -gt 0 ]] ; then
	core_path="$libretro_path$1$core_extension"
else
	echo "Wrong number of arguments provided"
	exit 1
fi

if [[ $# -eq 2  ]] ; then
	retroarch -f -L $core_path $"$2"
elif [[ $# -eq 3 ]] ; then
	retroarch -f -L $core_path -c $"$3" $"$2"
else
	echo "Wrong number of arguments provided"
	exit 1
fi
