.PHONY: build-deploy
build-deploy:
	@ docker build -f nginx/Dockerfile -t prakasa1904/nginx-service-export .
	@ docker push prakasa1904/nginx-service-export

.PHONY: run-dev
run-dev:
	@ docker-compose down --remove-orphans
	@ docker-compose up -d

.PHONY: show-log
show-log:
	@ docker-compose logs -f

.PHONY: down-dev
down-dev:
	@ docker-compose down --remove-orphans

.PHONY: prepare-attack
prepare-attack:
	@ which pip3 || exit 1
	@ pip3 install virtualenv
	@ python3 -m venv python_modules
	( \
		source python_modules/bin/activate; \
		pip install --upgrade pip; \
		pip install -r attacker/requirements.txt; \
	)

.PHONY: attack-me
attack-me:
	@ python3 -m venv python_modules
	( \
		source python_modules/bin/activate; \
		locust --host=http://localhost --locustfile attacker/main.py; \
	)
