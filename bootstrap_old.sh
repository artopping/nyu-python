#!/usr/bin/env bash

apt-get install build-essential gcc --assume-yes
apt-get update --fix-missing
apt-get install vim wget git zlib1g-dev --assume-yes
apt-get install python3 --assume-yes
apt-get install python3-venv --assume-yes
apt-get install bpython --assume-yes
apt-get install python
apt-get install python3-tk --assume-yes


# Pip3
apt-get install python3-pip --assume-yes
pip3 install --upgrade pip 
pip3 install numpy
pip3 install pandas 
pip3 install xlrd
pip3 install matplotlib


pip3 list --outdated --format=freeze
pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U


export RUN_USER="ubuntu"
export RUNUSER_PROG="/sbin/runuser"

export COMMAND=$(cat <<-'HERE1a'
    echo "\"echo \"in .profile\" >> $HOME/.profile\""
    echo "\"echo \"in .bashrc\" >> $HOME/.bashrc\""

    # xauth with complain unless ~/.Xauthority exists
    touch ~/.Xauthority

    # only this one key is needed for X11 over SSH 
    xauth generate :0 . trusted 

    # generate our own key, xauth requires 128 bit hex encoding
    xauth add ${HOST}:0 . $(xxd -l 16 -p /dev/urandom)

    # To view a listing of the .Xauthority file, enter the following 
    xauth list 
HERE1a
)


${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"
