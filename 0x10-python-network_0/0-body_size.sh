#!/bin/bash
# send a get request and
# get body size in bytes

curl -s -o file.txt $1
respond=$(wc -c < "file.txt")
echo $respond

