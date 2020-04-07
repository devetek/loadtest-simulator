SERVICE :=zeus

.PHONY: build-deploy
build-deploy: .validator
	@ docker build -f nginx/Dockerfile -t prakasa1904/nginx-service-export .
	@ docker push prakasa1904/nginx-service-export

.PHONY: run-dev
run-dev: .validator
	@ ./generator/main.sh $(SERVICE)
	@ docker-compose down --remove-orphans
	@ docker-compose up -d

.PHONY: show-services
show-services: .validator
	@ docker-compose ps --all

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
	# locust --host=http://localhost --locustfile attacker/main.py $(SERVICE);
	@ python3 -m venv python_modules
	( \
		export SERVICE=$(SERVICE); \
		source python_modules/bin/activate; \
		locust --host=http://localhost --locustfile attacker/main.py; \
	)

.PHONY: .validator
.validator:
	$(eval WHICH_DOCKER := $(shell which docker))
	$(eval WHICH_COMPOSE := $(shell which docker-compose))
	$(eval WHICH_PY3 := $(shell which python3))
	$(eval WHICH_VENV := $(shell which virtualenv))

	@ test -n "$(WHICH_DOCKER)" || sh -c 'echo "No docker binary, follow this link to install in mac https://docs.docker.com/docker-for-mac/install/" && exit 1'
	@ test -n "$(WHICH_COMPOSE)" || sh -c 'echo "No compose binary, follow this link to install in mac https://docs.docker.com/docker-for-mac/install/" && exit 1' 
	@ test -n "$(WHICH_PY3)" || sh -c 'echo "No python3 binary, follow this link to install in mac https://docs.docker.com/compose/install/" && exit 1'
	@ test -n "$(WHICH_VENV)" || sh -c 'echo "No virtualenv binary, follow this link to install in mac https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3" && exit 1'
