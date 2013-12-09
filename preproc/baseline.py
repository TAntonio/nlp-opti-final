#!/usr/bin/python
#
# baseline.py
#
# preprocesses tweets into random clusters for a baseline
from __future__ import division

import sys, os, subprocess, random


def main():
    feels=["happy","content","sad","angry"]
    happy=[]
    content=[]
    sad=[]
    angry=[]
    tweets=open("../data/tweet-bags","r+").readlines()
    subprocess.call("touch ../data/baseline-classification".split())
    bl=open("../data/baseline-classification","w+")
    for item in tweets:
        choice=random.choice(feels)
        if choice == "happy":
            happy.append(item.split()[0])
        elif choice == "content":
            content.append(item.split()[0])
        elif choice == "sad":
            sad.append(item.split()[0])
        elif choice == "angry":
            angry.append(item.split()[0])

    bl.write("happy:\n"+str(happy)+"\n")
    bl.write("content:\n"+str(content)+"\n")
    bl.write("sad:\n"+str(sad)+"\n")
    bl.write("angry:\n"+str(angry)+"\n")

    #correct, incorrectly-labeled-as, incorrectly-labeled
    happystats=[0,0,0]
    contentstats=[0,0,0]
    sadstats=[0,0,0]
    angrystats=[0,0,0]

    labeled=open("../data/labeled","r+").readlines()
    for i in range(len(labeled)):
        lsplit=labeled[i].split(" ")
        if len(lsplit) == 1:
            date=labeled[i-1].split(" ")[0]
            randomguess=""
            if date in happy:
                randomguess="happy"
            elif date in content:
                randomguess="content"
            elif date in sad:
                randomguess="sad"
            elif date in angry:
                randomguess="angry"

            if randomguess == lsplit[0]:
                if randomguess=="happy":
                    happystats[0]+=1
                elif randomguess=="content":
                    contentstats[0]+=1
                elif randomguess=="sad":
                    sadstats[0]+=1
                elif randomguess=="angry":
                    angrystats[0]+=1

            else:
                if randomguess=="happy":
                    happystats[1]+=1
                if randomguess=="content":
                    contentstats[1]+=1
                if randomguess=="sad":
                    sadstats[1]+=1
                if randomguess=="angry":
                    angrystats[1]+=1

                if lsplit[0]=="happy":
                    happystats[2]+=1
                if lsplit[0]=="content":
                    contentstats[2]+=1
                if lsplit[0]=="sad":
                    sadstats[2]+=1
                if lsplit[0]=="angry":
                    angrystats[2]+=1

    tp=happystats[0]+contentstats[0]+sadstats[0]+angrystats[0]
    fp=happystats[1]+contentstats[1]+sadstats[1]+angrystats[1]
    fn=happystats[2]+contentstats[2]+sadstats[2]+angrystats[2]

    #print str(tp)+" "+str(fp)+" "+str(fn)

    prec=tp/(tp+fp)
    rec=tp/(tp+fn)
    
    #print str(prec)+" "+str(rec)
    
    if rec==0.0 and prec==0.0:
        print("No true positives from random baseline.")
        bl.write("No true positives from random baseline.")
        sys.exit(1)

    f=2*(prec*rec)/(prec+rec)

    
    total=len(tweets)

    bl.write("stats:\n")
    bl.write("total accuracy: "+str(tp/total)+"\n")
    bl.write("total predicted happy: "+str(len(happy))+" ("+str(100*len(happy)/total)+"%)\n")
    bl.write("total predicted content: "+str(len(content))+" ("+str(100*len(content)/total)+"%)\n")
    bl.write("total predicted sad: "+str(len(sad))+" ("+str(100*len(sad)/total)+"%)\n")
    bl.write("total predicted angry: "+str(len(angry))+" ("+str(100*len(angry)/total)+"%)\n")

    bl.write("precision: "+str(prec)+"\n")
    bl.write("recall: "+str(rec)+"\n")
    bl.write("f-measure: "+str(f)+"\n")


if __name__=="__main__":
    main()
