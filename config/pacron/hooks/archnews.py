#! /usr/bin/python3

import subprocess
from datetime import datetime
import sys
import re

try:
    import feedparser
except:
    sys.exit('This program requires feedparser (python 3.x)')

def main():
    if len(sys.argv) > 1:
        try:
            lastUpgradeDate = datetime.strptime(sys.argv[1], '%m-%d-%Y')
        except ValueError:
            sys.exit('Argument must be of format: mm-dd-yyyy')
    else:
        lastUpgradeDate = getLastUpgradeDate()

    feed = feedparser.parse('https://www.archlinux.org/feeds/news/')
    latestNewsDate = getLatestNewsDate(feed)

    print('Last upgraded on {}'.format(lastUpgradeDate.strftime('%c')))

    if latestNewsDate >= lastUpgradeDate:
        news = getNewsSince(lastUpgradeDate, feed)
        for n in news:
            print('-' * 60)
            printEntry(n)
            if not confirm('Did you read this?'):
                sys.exit(1)
        print('-' * 60)
    else:
        print('No news.')

def getLastUpgradeDate():
    dt = subprocess.check_output('grep "starting full system upgrade" /var/log/pacman.log | tail -n1 | cut -d" " -f-2',
                                 shell=True, universal_newlines=True).strip()
    try:
        return datetime.strptime(dt, '[%Y-%m-%d %H:%M]')
    except ValueError:
        if len(dt) == 0:
            print('No system upgrade found. Not fetching Arch News.')
            sys.exit(0)
        else:
            sys.exit('Failed parse system upgrade time: {!r}'.format(dt))

def getLatestNewsDate(feed):
    return newsToDateTime(feed.entries[0])

def newsToDateTime(entry):
    return datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z').replace(tzinfo=None)

def getNewsSince(date, feed):
    return filter(lambda e: newsToDateTime(e) >= date, feed.entries)

def printEntry(entry):
    summary = re.sub('<[^<]+?>', '', entry.summary)
    summary = re.sub('\n+','\n\n', summary.strip())
    date = newsToDateTime(entry)
    datestr = date.strftime('%d %b %Y')
    print('{}\t({})\n\n{}\n\n{}'.format(entry.title, datestr, summary, entry.link))

def confirm(prompt=None, resp=False):
    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '{} [{}/{}]: '.format(prompt, 'Y', 'n')
    else:
        prompt = '{} [{}/{}]: '.format(prompt, 'y', 'N')

    while True:
        ans = input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print('please enter y or n.')
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False

if __name__ == '__main__':
    main()
