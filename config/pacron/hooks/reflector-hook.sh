#! /bin/bash

trap "exit 1" SIGINT

if ! hash reflector 2> /dev/null; then
    echo "This script requires reflector." >&2
    exit 1
fi

line=$(grep -n "Running 'pacman" /var/log/pacman.log | grep -v '\-U' | tail -n 1 | cut -d: -f1)

if [ -n "$1" ] || [ -n "$(sed "1,$(($line - 1))d" /var/log/pacman.log | grep -o 'upgraded pacman-mirrorlist')" ]; then
    echo 'Backing up old mirrorlist...'
    sudo cp -v /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.old
    echo 'Generating new /etc/pacman.d/mirrorlist...'
    sudo reflector -p https -f 10 --sort rate --save /etc/pacman.d/mirrorlist
    # TODO: delete mirrorlist.pacnew?
    echo 'Done!'
fi

