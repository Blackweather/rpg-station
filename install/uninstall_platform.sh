#!/bin/sh
# this script uninstalls the libretro core specified as input parameter
# example usage: ./uninstall_platform.sh nestopia
LIBPLAT=$(echo "$1_libretro")

PLATCHECK=$(ls /usr/lib/arm-linux-gnueabihf/libretro/. | grep $1)
if [[ -z "$PLATCHECK"  ]] ; then
	echo "$LIBPLAT is not installed"
else
	sudo rm "/usr/lib/arm-linux-gnueabihf/libretro/$LIBPLAT.so"
	
	PLATCHECK2=$(ls ~/libretro-super/dist/unix | grep $1)
	if [[ -z "$PLATCHECK2" ]] ; then
		echo "$LIBPLAT is not builded"
	else
		sudo rm "~/libretro-super/dist/unix/$LIBPLAT.so"
	fi
fi
