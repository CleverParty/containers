project:
	echo "Running python files"

build:
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
	bash ~/miniconda.sh -b -p $HOME/miniconda
	conda create -n fenicsproject -c conda-forge fenics
	source activate fenicsproject
	pip install nashpy
	# pip install numpy
	#pip install matplotlib
	pip install sympy
	pip freeze
	python3 interface/holder/canaryTest.py
	# source game/bin/activate , Using a "." instead of source works 
	python3 nash/actors.py
