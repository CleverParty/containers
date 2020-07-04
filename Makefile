project:
	echo "Running python files"

build:
	. game/bin/activate # Using a "." instead of source works , also this env has all required packages currently
	python3 nash/actors.py
