#!/bin/bash

local_workdir=$(cd $(dirname $(dirname $(dirname "${BASH_SOURCE[0]}"))) >/dev/null 2>&1 && pwd)

main() {
  local container_workdir=/app
  local container_name=dummy
  docker run --rm -it \
    --name $container_name \
    --volume $local_workdir:$container_workdir \
    --workdir $container_workdir \
    --network custom_network \
    dummyapis \
    sh
}

main