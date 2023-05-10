CC=python
CC_PACKAGE=pip

install:

	$(CC_PACKAGE) install -r requirements.txt
	pyinstaller --onefile docker.py templates.py utils.py dockerbuilder.py -n dockerbuilder

	echo Binary avaliable in /dist directory