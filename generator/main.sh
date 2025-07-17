#!/bin/sh

SERVICE=$1

pre_requirement() {
    # Generate up access log
    cp -rf nginx/access-log-exporter/${SERVICE}.yml nginx/access-log-exporter/up.yml
}

pre_requirement