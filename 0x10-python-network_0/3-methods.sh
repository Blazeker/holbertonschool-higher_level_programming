#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -sIX OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '