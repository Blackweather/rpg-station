#!/bin/bash
# this script manages initial configuration
# and dependencies

# prepare system
sudo apt-get -y upgrade
sudo apt-get -y install software-properties-common build-essential flatpak
sudo apt-get -y update

# check if python3 is installed
PYCHECK=$(which python3)
if [[ "$PYCHECK" != "/usr/bin/python3" ]] ; then
	sudo apt-get -y install checkinstall
	sudo apt-get -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
	CURRENTPATH=$(pwd)
	cd /usr/src
	sudo wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
	sudo tar xzf Python-3.7.3.tgz
	cd Python-3.7.3
	sudo ./configure --enable-optimizations
	sudo make altinstall
	cd $CURRENTPATH
	sudo apt-get -y update
else
	echo "Python 3 is installed"
fi

# check if pip3 is installed
PIPCHECK=$(which pip3)
if [[ "$PIPCHECK" != "/usr/bin/pip3" ]] ; then
	sudo apt-get -y install python3-pip
	sudo apt-get -y update
else
	echo "pip3 is installed"
fi

# make Python 3 default version of python command
PYCHECKDEF=$(python --version 2>&1)
if [[ "$PYCHECKDEF" =~ 2 ]] ; then
    echo -e "\nalias python='/usr/bin/python3'" >> ~/.bashrc
	. ~/.bashrc
	sudo apt-get -y update
else 
	echo "Default version of python is Python 3"
fi

# make pip3 default version of pip command
PIPCHECKDEF=$(pip -V)
if [[ "$PIPCHECKDEF" != "pip 18.1 from /usr/lib/python3/dist-packages (python 3.7)" ]] ; then
	echo -e "\nalias pip='/usr/bin/pip3'" >> ~/.bashrc
	. ~/.bashrc
	sudo apt-get -y update
else 
	echo "Default version of pip is pip3"
fi

# check that libretro-super is downloaded
LSCHECK=$(ls ~/. | grep libretro-super)
if [[ -z "$LSCHECK" ]] ; then
	
	sudo apt-get -y install libxkbcommon-dev zlib1g-dev libfreetype6-dev \
	ibegl1-mesa-dev libgles2-mesa-dev libgbm-dev libavcodec-dev \
	libsdl2-dev libsdl-image1.2-dev libxml2-dev yasm git
	CURRENTPATH=$(pwd)
	cd ~/.
	# download libretro-super to ~/liberetro-super
	git clone git://github.com/libretro/libretro-super.git
	cd libretro-super
	SHALLOW_CLONE=1 ./libretro-fetch.sh
	cd $CURRENTPATH
fi
	
# check that retroarch installed
RACHECK=$(flatpak list | grep org.libretro.RetroArch)
if [[ -z "$RACHECK" ]] ; then
	flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
	flatpak install -y flathub org.libretro.RetroArch
	flatpak update
fi
