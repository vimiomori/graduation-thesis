#!/bin/bash

python3 --version

if [ $? -ne 0 ]
then
	echo 'Python3 not installed'
	echo 'Installing python3'
	sudo apt install python3 python3-pip
fi

echo 'Installing venv'
sudo apt install python3-venv
echo 'Initiating virtual environment'
python3 -m venv .venv
source .venv/bin/activate
echo 'Installing dependencies'
pip3 install -r requirements.txt

echo 'Setup complete babyyyy'
