project:
	echo "Running python files"

build:
	pip install nashpy
	# pip install numpy
	#pip install matplotlib
	pip install sympy
	python3 interface/holder/diffTest.py
	python3 interface/manage.py test
	# source game/bin/activate , Using a "." instead of source works 
	python3 nash/actors.py
