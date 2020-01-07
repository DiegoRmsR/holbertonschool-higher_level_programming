#!/bin/bash
# cURL only methods 
curl -si "$1" | head -3 | tail -1 | cut -d " " -f2-
