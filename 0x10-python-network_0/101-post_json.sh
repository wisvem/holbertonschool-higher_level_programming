#!/bin/bash
# Task 8
curl -H "Content-Type: application/json" -sd @"$2" "$1"
