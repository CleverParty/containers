project:
	echo "Running python files"

build:
	pip install nashpy
	# pip install numpy
	#pip install matplotlib
	pip install sympy
	pip freeze
	python3 interface/holder/canaryTest.py
	# source game/bin/activate , Using a "." instead of source works 
	python3 nash/actors.py
