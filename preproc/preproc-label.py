#!/usr/bin/python
#
# preproc-label.py
#
# prepares 2 weeks of tweets for labeling

import sys, os, subprocess

def main():
    tweets=open("../data/tweets.txt", 'r+').readlines()
    subprocess.call("touch ../data/labeled".split(" "))
    to_label=open("../data/labeled", 'w+')
    for item in tweets:
        date=item.split(" ")[0]
        datesplit=date.split("/")
        if int(datesplit[1]) == 11:
            if int(datesplit[0]) < 22:
                break
        to_label.write(item)


if __name__=="__main__":
    main()
