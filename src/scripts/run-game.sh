#!/bin/bash
# this scripts run the specified rom file
# with a specified libretro core
# example usage: ./run-game.sh gambatte ../../rom/gb/adjustris.gb

# TODO: change the path to standard path on raspbian
libretro_path='/usr/lib/x86_64-linux-gnu/libretro/'
core_extension='_libretro.so'
core_path="$libretro_path$1$core_extension"

retroarch -f -L $core_path $2
