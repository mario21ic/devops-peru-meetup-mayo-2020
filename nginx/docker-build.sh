#!/bin/bash

VERSION="1.0"
if [ ! -z $1 ]; then
    VERSION=$1
fi
docker build --build-arg VERSION=$VERSION -t mario21ic/nginx:light-$VERSION .
