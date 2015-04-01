#! /bin/bash

line=$(grep -n "Running 'pacman" /var/log/pacman.log | grep -v '\-U' | tail -n 1 | cut -d: -f1)

sed "1,$(($line - 1))d" /var/log/pacman.log

