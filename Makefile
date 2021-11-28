install-virtualenv:
	rm -rf local.virtualenv
	virtualenv -p python3.9 local.virtualenv
	./local.virtualenv/bin/pip install setuptools pip wheel -U
	./local.virtualenv/bin/pip install -r requirements.txt --find-links "file://${HOME}/.pip/wheelhouse"

shell:
	./local.virtualenv/bin/python3.9 manage.py shell

run-server:
	./local.virtualenv/bin/python3.9 manage.py runserver
