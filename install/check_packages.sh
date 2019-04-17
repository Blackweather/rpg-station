#!/bin/bash
# quick check for retroarch installed packages
dpkg --list | grep -E -o '(retroarch.*|libretro.*)' | tr -s ' ' | cut -d ' ' -f 1
