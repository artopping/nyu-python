apt-get update --fix-missing
apt-get install vim git zlib1g-dev build-essential gcc --assume-yes

cd /home/vagrant/
sudo wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
sudo tar -xvf Python-3.6.1.tar.xz
cd Python-3.6.1
sudo ./configure
make
sudo make install

#!/usr/bin/env bash

#these are new additions 6/14/17 with bootstrap.sh from class git repo
apt-get update --fix-missing
apt-get install vim git zlib1g-dev --assume-yes
apt-get install python3 --assume-yes
apt-get install python3-venv --assume-yes
apt-get install bpython --assume-yes
apt-get install bpython --assume-yes

###su - vagrant -c "cd /home/vagrant && mkdir dev && cd dev && git clone https://github.com/robmarano/nyu-python.git"
