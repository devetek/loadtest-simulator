.PHONY: build-deploy
build-deploy: .validator
	@ docker build -f nginx/Dockerfile -t prakasa1904/nginx-service-export .
	@ docker push prakasa1904/nginx-service-export

.PHONY: run-dev
run-dev: .validator
	@ docker-compose down --remove-orphans
	@ docker-compose up -d

.PHONY: show-log
show-log: .validator
	@ docker-compose logs -f

.PHONY: down-dev
down-dev: .validator
	@ docker-compose down --remove-orphans

.PHONY: prepare-attack
prepare-attack: .validator
	@ which pip3 || exit 1
	@ pip3 install virtualenv
	@ python3 -m venv python_modules
	( \
		source python_modules/bin/activate; \
		pip install --upgrade pip; \
		pip install -r attacker/requirements.txt; \
	)

.PHONY: attack-me
attack-me: .validator
	@ python3 -m venv python_modules
	( \
		source python_modules/bin/activate; \
		locust --host=http://localhost --locustfile attacker/main.py; \
	)

.PHONY: .validator
.validator:
	$(eval WHICH_DOCKER := $(shell which docker))
	$(eval WHICH_COMPOSE := $(shell which docker-compose))
	$(eval WHICH_PY3 := $(shell which python3))
	$(eval WHICH_VENV := $(shell which virtualenv))

	@ test -n "$(WHICH_DOCKER)" || echo "No docker binary"
	@ test -n "$(WHICH_COMPOSE)" || echo "No compose binary"
	@ test -n "$(WHICH_PY3)" || echo "No python3 binary"
	@ test -n "$(WHICH_VENV)" || echo "No virtualenv binary"
