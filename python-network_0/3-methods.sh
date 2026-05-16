#!/bin/bash
# Displays HTTP methods allowed by the server
curl -sI "$1" | grep -i "allow:" | cut -d ' ' -f2-
