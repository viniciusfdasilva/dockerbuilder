CC=python
CC_PACKAGE=pip

args = $(foreach a,$($(subst -,_,$1)_args),$(if $(value $a),$a="$($a)"))

run:
@echo args
ifneq ($(shell id -u), 0)
	@echo "You are not root, run this target as root please"
	@exit 0
else
	@python -m venv venv > /dev/null
	. venv/bin/activate > /dev/null
	@pip install -r requirements.txt > /dev/null

	@python manage.py migrate > /dev/null
	@python dockerbuilder.py -l

endif