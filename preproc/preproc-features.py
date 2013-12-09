#!/usr/bin/python
#
# preproc-features.py
#
# organizing the things that go in the feature vector

import sys, os, subprocess

def main():
    wnaffpre=open("../data/a-hierarchy.xml","r+").readlines()
    wnaff=[]
    for line in wnaffpre:
        if len(line.split()) == 3:
            wnaff.append(line)

    subprocess.call("touch ../data/affective-features".split())
    aff=open("../data/affective-features","w+")
    happy=["joy","love","enthusiasm","self-pride","fearlessness"]
    content=["affection","liking","gratitude","levity","calmness"]
    sad=["sadness","negative-fear","shame","despair","daze"]
    angry=["general-dislike","anxiety"]
    feels=[happy,content,sad,angry]

        #print linesplit
    for f in feels:
        for h in f:
            subcat=[]
            
            for line in wnaff:
                linesplit=line.split()
                #print linesplit[2][5:-3]
                if linesplit[2].count(h) > 0 or linesplit[2][5:-3] in subcat:
                    emotion=linesplit[1][6:-1]
                    aff.write(h+": "+linesplit[1][6:-1]+"\n")
                    #print emotion
                    subcat.append(emotion)
        aff.write("----\n")


if __name__=="__main__":
    main()
