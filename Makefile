CC=python
CC_PACKAGE=pip

install:

ifneq ($(shell id -u), 0)
	@echo "You are not root, run this target as root please"
	@exit 0
else

ifeq ($(shell docker info | grep buildx:), "  buildx: Docker Buildx (Docker Inc.)")
	@echo "Docker is not installed! Please install docker to continue"
else

ifeq ($(shell systemctl is-active docker), "inactive")
	@systemctl start docker.service
	@systemctl start docker.socket
endif
	$(CC_PACKAGE) install -r requirements.txt
	@pyinstaller --onefile docker.py templates.py utils.py dockerbuilder.py -n dockerbuilder
	@cp dist/dockerbuilder /usr/bin
	@rm -r build dist
	@echo "======================================================="
	@echo Installation sucessfuly! Please try run 'dockerbuilder'
	@echo "======================================================="
endif
endif