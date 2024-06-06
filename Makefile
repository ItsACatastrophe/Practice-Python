install:
	cat .python-version | pyenv install -s
	pip install -r requirements.txt