#!/bin/sh
# this script installs the libretro core specified as input parameter
# example usage: ./install_platform.sh nestopia

# define platform package name
LIBPLAT=$(echo "$1_libretro")

# check if platform is installed
PLATCHECK=$(ls /usr/lib/arm-linux-gnueabihf/libretro/. | grep $1)
if [[ "$PLATCHECK" != "$LIBPLAT.so" ]] ; then
	
	# check if core is built
	PLATCHECK2=$(ls ~/libretro-super/dist/unix | grep $1)
	if [[ "$PLATCHECK2" != "$LIBPLAT.so" ]] ; then
		# build specified core
		sudo . ~/libretro-super/libretro-build.sh $1
	fi
	
	# install built core
	sudo cp "~/libretro-super/dist/unix/$LIBPLAT.so" "/usr/lib/arm-linux-gnueabihf/libretro/."\
else
	echo "$LIBPLAT is installed"
fi
