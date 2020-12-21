project:
	echo "Running python files"
test:
	echo "test Phase has begun"
build:
	pip3 install --upgrade pip
	pip3 install --upgrade setuptools
	pip3 install websocket_client
	pip3 install nashpy
	pip3 install websocket
	pip3 install matplotlib
	pip3 install sympy
	pip3 install beautifulsoup4
	pip3 install pandas-datareader
	pip3 install tensorflow
	pip3 install keras
	pip3 install finnhub-python
	pip3 install sklearn
	pip3 install finnhub-python
	# pip3 install plotit , dependency for tickerScanner.py
	# source game/bin/activate , Using a "." instead of source also works
	python3 nash/actors.py
	go build main.go
	# ./start_server.sh
dynamic:
	# re-read PEP 20 for code practices, and then read PEP 20 again.
	# in koyfin, track gold fluctuations
	# utilize, quantconnect for factor analysis and back-testing
	# python3 nash/poker.py
	# python3 algos/lychrel.py
	# python3 algos/frequentDigits.py
	python3 algos/reverseDigits.py
	echo "reversing digits works"
	python3 algos/squareConvergents.py
	python3 algos/maxProfit.py
	echo "algo test sequence"
	# python3 data/tickerScanner.py
	python3 data/tickerPackageStaging.py
	# python3 data/arithproj.py
	# python3 interface/holder/canaryTest.py
