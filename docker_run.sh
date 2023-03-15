#!/usr/bin/env bash

# Always be sure we are loggued in docker
if [ ! -f /root/.docker/config.json ]; then
   echo "Login to docker with credentials naparuba"
   docker login --username naparuba --password $DOCKER_TOKEN
fi

MODE="$1"
DF="$2"
PYTHON3_ARGS=""
if [ "$3" == "python3" ]; then
   PYTHON3_ARGS=" --build-arg=MY_PYTHON_VERSION=-python3"
fi


if [ $MODE == "test" ]; then
   # -p 8000:8000
   docker run --env-file ~/.docker_env -v /dev:/dev --rm=true --privileged --cap-add ALL -v /root/blog/output:/root/blog/output --tty --interactive --entrypoint=/bin/bash $(docker build -t $DF -q -f $DF $PYTHON3_ARGS . | cut -d':' -f2)
   exit $?
fi

if [ $MODE == "run" ]; then
   docker run --env-file ~/.docker_env -p 8000:8000 --rm=true --privileged --cap-add ALL -v /root/blog/output:/root/blog/output --tty --interactive $(docker build -t $DF -q -f $DF $PYTHON3_ARGS . | cut -d':' -f2)
   exit $?
fi

if [ $MODE == "build" ]; then
   docker build -t $DF -f $DF $PYTHON3_ARGS .
   exit $?
fi

