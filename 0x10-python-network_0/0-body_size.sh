#!/bin/bash
# Get the content-length of the response headers
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
