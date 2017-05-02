#!/bin/sh

if [ ! -d "venv" ]; then
	python3 -m venv venv
	. ./venv/bin/activate
	pip3 install Django
	pip3 install requests
fi

. ./venv/bin/activate
python3 ./manage.py runserver

