# pacron

PACman Run ON is a basic wrapper for Arch Linux's pacman to provide simple hooks for other scripts and commands. It's loosely modeled off of [cron](http://linux.die.net/man/5/crontab), the GNU/Linux utility, in which a "tab" file controls when commands are run.

## Features
* Wraps `pacman` and also [`packer`](https://github.com/keenerd/packer/wiki)
* Automatically runs scripts before or after `pacman`/`packer` executes
* Uses bash pattern matching on options passed to `pacman`/`packer` to choose which commands to run

## Usage
```
usage: pacron [options]

PACman Run ON, the pacman hook wrapper | www.github.com/kevlar1818/pacron

Copyright 2014 Kevin Hanselman (See LICENSE or source)

Options:
  -h		show this help text and exit
  -e		edit ~/.config/pacron/pacrontab
```

## The `pacrontab`
```
# ~/.config/pacron/pacrontab
-Qi   before  $HOME/.config/pacron/hooks/print-args.sh "called before"
-Q*   after   ~/.config/pacron/hooks/print-args.sh "called after"
```
Each row of the `pacrontab` is made up of whitespace separated columns. The first column of each row is the option pattern to run on. The second column is either 'before' or 'after', indicating whether the command is run before or after `pacman`/`packer` executes. The third column and beyond is the commands/script and arguments to run.

To see an example `pacrontab`, check out [the source](https://github.com/kevlar1818/pacron/blob/master/example-config/pacrontab).

## Quick Setup
```
cd && git clone https://github.com/kevlar1818/pacron .pacron-git
mkdir -p ~/.config
cp -r .pacron-git/example-config .config/pacron
```

## Contributing
Yes, please do! Pull request away.

## Important!
This repository is strictly a work in progress. It has a long way to go before it's good enough for serious use.
