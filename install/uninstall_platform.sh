#!/bin/sh
# this script uninstalls the libretro core specified as input parameter
# example usage: ./uninstall_platform.sh nestopia

# define platform package name
LIBPLAT=$(echo "$1_libretro")

# check that if platform is installed
PLATCHECK=$(ls /usr/lib/arm-linux-gnueabihf/libretro/. | grep $1)
if [[ -z "$PLATCHECK"  ]] ; then
	echo "$LIBPLAT is not installed"
else
	# remove builded core from retroarch
	sudo rm "/usr/lib/arm-linux-gnueabihf/libretro/$LIBPLAT.so"
	
	# check if core is builded
	PLATCHECK2=$(ls ~/libretro-super/dist/unix | grep $1)
	if [[ -z "$PLATCHECK2" ]] ; then
		echo "$LIBPLAT is not builded"
	else
		# remove builded core
		sudo rm "~/libretro-super/dist/unix/$LIBPLAT.so"
	fi
fi
