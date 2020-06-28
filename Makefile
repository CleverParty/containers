project:
	echo "Running python files"


build:
	. game/bin/activate # Using a "." instead of source works !
	python3 nash/actors.py
