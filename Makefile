install-virtualenv:
	rm -rf local.virtualenv
	virtualenv -p python3.9 local.virtualenv
	./local.virtualenv/bin/pip install setuptools pip wheel -U
	./local.virtualenv/bin/pip install -r requirements.txt --find-links "file://${HOME}/.pip/wheelhouse"

run-server:
	docker-compose run web

test:
	docker-compose run test

migrate:
	docker-compose run migrate

coverage:
	docker-compose run coverage
