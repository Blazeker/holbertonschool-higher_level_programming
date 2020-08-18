#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
