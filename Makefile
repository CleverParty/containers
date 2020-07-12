project:
	echo "Running python files"

build:
	pip3 install nashpy
	# pip install numpy
	# pip install matplotlib
	pip3 install sympy
	pip3 freeze
	python3 interface/holder/canaryTest.py
	# source game/bin/activate , Using a "." instead of source works 
	python3 nash/actors.py
