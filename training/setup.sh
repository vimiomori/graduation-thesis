#!/bin/bash

python3 --version

if [ $? -ne 0 ]
then
	echo 'Python3 not installed'
	echo 'Installing python3'
	apt -y update
	apt -y upgrade
	apt install -y python3 python3-pip
fi

echo 'Installing jq'
apt-get install jq
echo 'Installing venv'
apt install -y python3-venv
echo 'Initiating virtual environment'
python3 -m venv .venv
source .venv/bin/activate
echo 'Installing dependencies'
pip3 install -r requirements.txt

echo 'Setup complete babyyyy'
