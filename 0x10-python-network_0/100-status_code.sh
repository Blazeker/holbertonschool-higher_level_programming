#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -s -o /dev/null -I -w "%{http_code}" "$1"
