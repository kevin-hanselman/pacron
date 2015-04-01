#!/bin/bash

confirm() {
    # call with a prompt string or use a default
    read -r -p "${1:-Continue? [y/N]} " response
    case $response in
        [yY][eE][sS]|[yY]) return 0 ;;
        *) return 1 ;;
    esac
}

if [ -n "$( last-pacman-log.sh | grep -o 'upgraded linux (')" ]; then
    confirm 'The Linux kernel has been upgraded. Reboot now? [y/N] ' || exit 0
    sudo reboot
fi

