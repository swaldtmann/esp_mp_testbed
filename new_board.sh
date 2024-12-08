#!/bin/sh

# Erase board
pipenv run erase-flash

# Flash firmware
pipenv run flash-s3
# Transfer code
pipenv run sync-code
