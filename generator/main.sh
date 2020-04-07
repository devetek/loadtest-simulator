#!/bin/sh

SERVICE=$1

pre_requirement() {
    # Generate background process
    nginx/process/supervisor.template ${SERVICE} > nginx/process/supervisor.conf
}

pre_requirement