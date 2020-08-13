project:
	echo "Running python files"
test:
	echo "test Phase has begun"
build:
	pip3 install nashpy
	pip3 install numpy
	pip3 install matplotlib
	pip3 install sympy
	pip3 install beautifulsoup4
	pip3 install pandas-datareader
	# source game/bin/activate , Using a "." instead of source also works 
	# python3 nash/actors.py
	# ./start_server.sh
dynamic:
	# python3 nash/poker.py
	# python3 algos/lychrel.py
	python3 algos/frequentDigits.py
	python3 algos/squareConvergents.py
	python3 interface/holder/canaryTest.py
	python3 scrapeHistoricalData.py
