#! /bin/bash

echo "Hook called!"
echo "Arguments:"
for arg in "$@"; do
    echo "$arg"
done
