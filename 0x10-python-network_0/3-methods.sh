#!/bin/bash
# cURL only methods 
curl -sI "$1" | head -n4 | tail -n1 | cut -d " " -f2-
