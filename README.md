# How To Use

### Before start

For mac OS, please install python3, virtualenv, docker, docker-compose. You can follow link bellow before start:
- [python3 and virtualenv](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Docker-Compose](https://docs.docker.com/compose/install/)


### How To Develop Your Own

Create file under `attacker/task`, for example `zes.py` or `atreus.py`. Then create your own data from `attacker/data`, on this path also create your own data, for example `atreus.py`. After 2 file created, then edit file task you create previously, then import your data.

After attacker created, please create your own exporter config here `nginx/access-log-exporter/lite-atreus.yml`. Edit the file base on your service/path requirement.

### Running All Requirement

```sh
make run-dev SERVICE=zeus
make run-dev SERVICE=atreus
```

After execute command above you will have port open in `9090`, `9100`, `9093`, `8080`, `3000`, `80`, `4040`. So make sure that, the port does not open before this service up. And oh, I think you want to know, why we need open too much port. It will be amazing to have all of those service, trust me!.

Remember that, all of the port can be open in `localhost`, for example [Grafana](http://localhost:3000). With user (admin) and password (foobar) You know all of the basic now, then, we can continue to the next phase, below!.


### Running Attacker

```sh
make prepare-attack
make attack-me SERVICE=atreus
make attack-me SERVICE=zeus
```

This is the cool stuff, attacker is, the tools to help you make a load test to the service and make the grafana dashboard looks alive. After execute command above, you'll be have awesome locust dashboard under `http://*:8089`. Open the [locust dashboard](http://localhost:8089) and input some data to make load test to the service.


### Extra Dashboard To Collect RPS

Just simple query to adding rps:
```sh
sum(rate(lite_zeus_http_response_count_total[5m]))
```


### Contact When Have Problem

If you facing issue when running this service, visit me at [Terpusat](https://outletcyber.net)


### References
- [Prometheus](https://prometheus.io/docs/introduction/overview/)
- [Locust](https://docs.locust.io/en/stable/)