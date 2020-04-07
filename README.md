# How To Use

### How To Develop Your Own

Create file under `attacker/task`, for example `zes.py` or `atreus.py`. Then create your own data from `attacker/data`, on this path also create your own data, for example `atreus.py`. After 2 file created, then edit file task you create previously, then import your data. And then follow this step below to.

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
make attack-me
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