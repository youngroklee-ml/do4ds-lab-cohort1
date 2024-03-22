#!/bin/bash
docker build -t penguin-model docker/
docker run --rm -d \
  -p 8080:8080 \
  --name penguin-model \
  -v $(pwd)/data/model:/data/model \
  penguin-model
