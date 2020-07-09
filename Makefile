project:
	echo "Running python files"

build:
	pip install nashpy
	pip install numpy
	pip install matplotlib
	# source game/bin/activate , Using a "." instead of source works 
	python3 nash/actors.py
