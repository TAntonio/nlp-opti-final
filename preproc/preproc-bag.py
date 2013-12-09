#!/usr/bin/python
#
# preproc-bag.py
#
# turns a day of tweets into a bag of words.

import sys, os, subprocess
def main():
    subprocess.call("touch ../data/tweet-bags".split(" "))
    tweetbags=open("../data/tweet-bags", 'w+')
    tweets=open("../data/tweets.txt",'r+').readlines()
    
    initdate=tweets[0].split(" ")[0]
    wordlist=[]
    for item in tweets:
        date=item.split(" ")[0]
        if not date == initdate:
            tweetbags.write(initdate+" ")
            tweetbags.write(str(wordlist))
            tweetbags.write("\n")
            initdate=date
            wordlist=[]
        tweetsplit=item.split(" ")
        tweetsplit.pop(0)
        tweetsplit.pop(0)
        for word in tweetsplit:
            if word.endswith(("\r","\n")):
                word=word.rstrip("\r\n")
            if word.endswith("!"):
                if not "!" in wordlist:
                    wordlist.append("!")
                word=word.rstrip("!")
            if word.startswith((".","\"","/","*","(","~")):
                word=word.lstrip(".\"(*~")
            if word.endswith((",",".",";","\"","/","*","~")):
                word=word.rstrip(",.;\"/*~")
            if word.endswith("?") and not word.startswith("?"):
                word=word.rstrip("?")
            if word.endswith(")") and not word == ":)":
                word=word.rstrip(")")
            if word.endswith(":") and not word == "D:":
                word=word.rstrip(":")
            if word.startswith(":") and len(word) > 2:
                word=word.lstrip(":")
            
            if not word in wordlist:
                wordlist.append(word)
        



if __name__=="__main__":
    main()
