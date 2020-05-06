#!/usr/bin/env bash

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

echo "$dir"

sudo pip3 install Flask

sudo python3 $dir/app/app.py
