#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -s -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
