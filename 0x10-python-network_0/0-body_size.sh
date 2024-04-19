#!/bin/bash
# send a get request and
# get body size in bytes

temp_file=$(mktemp)
url=$1

curl -s -o "$temp_file" "$url"
respond=$(wc -c < "$temp_file")
echo $respond
rm "$temp_file"
