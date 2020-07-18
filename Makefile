project:
	echo "Running python files"
test:
	echo "test Phase has begun"
build:
	pip3 install nashpy
	# pip install numpy
	pip3 install matplotlib
	pip3 install sympy
	pip3 install beautifulsoup4
	pip3 freeze
	# source game/bin/activate , Using a "." instead of source works 
	python3 nash/actors.py
	# ./start_server.sh
dynamic:
	python3 interface/holder/canaryTest.py
	python3 scrapeHistoricalData.py