#!/bin/bash
cd /home/sergo/rnd || exit 1
git checkout master || exit 1
git pull origin master || exit 1
exec python3 my_random.py
