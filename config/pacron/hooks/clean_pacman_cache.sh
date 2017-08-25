#!/bin/bash

max_size="$1"

set -euo pipefail

[ -n "$max_size" ] || max_size=5

cache_size=$(du -s --block-size=1G /var/cache/pacman/ | awk '{print $1}')

if [ "$cache_size" -ge "$max_size" ]; then
    sudo pacman -Sc
fi
