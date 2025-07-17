# How To Use

### Before Start

For mac OS, please install python3, virtualenv, docker, docker-compose. You can follow link below before start:
- [python3 and virtualenv](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Docker-Compose](https://docs.docker.com/compose/install/)


### How To Develop Your Own

Create file under `attacker/task`, for example `atreus.py`. Then create data in `attacker/data`, for example create `atreus.py`. After 2 files created, then edit file task you created previously `attacker/task/atreus.py`, then import your data `from data.atreus import STATIC_DATA`.

After attacker created, please create service exporter config here `nginx/access-log-exporter/lite-atreus.yml`. Edit the file base on your service/path requirements.

### Running All Requirements

Execute command below to start all requirement services, for example if you want to start `atreus`:

```sh
make run-dev SERVICE=atreus
```

After execute command above you will have port open in `9090`, `9100`, `9093`, `8080`, `3000`, `80`, `4040`. So make sure that, the port does not open before this service up. And oh, I think you want to know, why we need open too much port. It will be amazing to have all of those service, trust me!.

Remember that, all of the port can be open in `localhost`, for example [Grafana](http://localhost:3000). With user (admin) and password (foobar) You know all of the basic now, then, we can continue to the next phase, below!.


### Running Attacker

After all require services up, you need to boot the attacker with command below:

```sh
make prepare-attack
make attack-me SERVICE=atreus
```

`make prepare-attack` used to setup virtual environment for your python. It will isolate the python module for this project from globals.

This is the cool stuff, attacker is, the tools to help you make a load test to the service and make the grafana dashboard looks alive. After execute command above, you'll be have awesome locust dashboard under `http://*:8089`. Open the [locust dashboard](http://localhost:8089) and input some data to make load test to the service.


### How To Debug

After services and attacker up, it will create some important file to help you investigate when facing issue. Focus on the folder `log`, there are have some files which can help you to debug when facing issue/error.

- log/access-log-exporter/access-log-exporter.log (if rps does not appears in grafana)
- log/nginx/access.log (nginx access log)
- log/nginx/error.log (if nginx got issue)
- log/supervisor (supervisor/manager log)


### How To Create Dashboard From File

Before start all of the service, you can create your own dashboad from provisioning folder `grafana/provisioning/dashboards`. Create your own json, or just copy paste from the existing and edit some related data, you know what I mean la....

Or if you want to create your ownn dashboard from scratch, just try use this simple query to collecting the rps:

```sh
sum(rate(lite_zeus_http_response_count_total[5m]))
```

### Contact When Have Problem

If you facing issue when running this service, visit me at [dPanel](https://cloud.terpusat.com)


### References
- [Prometheus](https://prometheus.io/docs/introduction/overview/)
- [Locust](https://docs.locust.io/en/stable/)
