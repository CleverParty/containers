project:
	echo "Running python files"

build:
	pip install nashpy
	. game/bin/activate # Using a "." instead of source works !
	python3 nash/actors.py
