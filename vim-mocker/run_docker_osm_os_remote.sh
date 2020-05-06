#!/usr/bin/env bash

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

echo "$dir"

sudo docker stop vim-mocker
sudo docker rm vim-mocker

sudo docker run -d --name vim-mocker \
    -p 4000:4000 \
    -p 10243:10243 \
    -p 9005:9005 \
    -p 6001:6001 \
    -p 9775:9775 \
    -p 10697:10697 \
    -v $dir:/app \
    --env MANO=osm \
    vim-mocker
