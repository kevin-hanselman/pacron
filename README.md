# pacron

PACman Run ON is a basic wrapper for Arch Linux's pacman to provide simple hooks for other scripts and commands. It's loosely modeled off of [cron](http://linux.die.net/man/5/crontab), the GNU/Linux utility, in which a "tab" file controls when commands are run.

## Features
* Wraps `pacman` and also [`packer`](https://github.com/keenerd/packer/wiki)
* Automatically runs scripts before or after `pacman`/`packer` executes
* Uses bash pattern matching on options passed to `pacman`/`packer` to choose which commands to run

## Hook Scripts
This is a list of currently implemented hooks for `pacron`. If you'd like to suggest a hook, use the [issue tracker](https://github.com/kevlar1818/pacron/issues). If you have a hook you'd like to share, [open a pull request](https://github.com/kevlar1818/pacron/pulls)!

- [x] Check and display recent Arch Linux news before performing a full system upgrade (`-Su`, `-Syu`, etc).
- [x] After performing a system upgrade, upgrade all vim plugins.

## The `pacrontab`
```
# ~/.config/pacron/pacrontab: table for pacron
# PATTERN   after/before    PATH
-S*u*       before          ~/.config/pacron/hooks/archnews.py
-S*u*       after           vim -c 'PluginUpdate' -c 'qa!'
```
Each row of the `pacrontab` is made up of whitespace separated columns. The first column of each row is the option pattern to run on. The second column is either 'before' or 'after', indicating whether the command is run before or after `pacman`/`packer` executes. The third column and beyond is the commands/script and arguments to run.

## Quick Setup
```
cd && git clone https://github.com/kevlar1818/pacron .pacron-git
mkdir -p ~/.config
cp -r .pacron-git/config/pacron ~/.config/pacron
```

## Usage
```
usage: pacron [options]

PACman Run ON, the pacman hook wrapper | www.github.com/kevlar1818/pacron

Copyright 2014 Kevin Hanselman (See LICENSE or source)

Options:
  -h		show this help text and exit
  -e		edit ~/.config/pacron/pacrontab
```

