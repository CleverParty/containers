project:
	echo "Running python files"

build:
	. game/bin/activate # Using a "." instead of source works !
	pip3 install nashpy
	python3 nash/actors.py
