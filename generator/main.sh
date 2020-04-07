#!/bin/sh

SERVICE=$1

pre_requirement() {
    # Generate up access log
    cp -rf nginx/access-log-exporter/lite-${SERVICE}.yml nginx/access-log-exporter/lite-up.yml
}

pre_requirement