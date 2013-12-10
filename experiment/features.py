#!/usr/bin/python
#
# features.py
#
# creates feature vectors with frequency counts

import sys, os, subprocess

def main():
    bags=open("../data/tweet-bags","r+").readlines()
    subprocess.call("touch ../data/featurevectors".split())
    feats=open("../data/featurevectors","w+")
    feels=open("../data/affective-features","r+").readlines()
    swearlex=open("../data/badwords.txt","r+").readlines()
    posemotes=open("../data/pos-emote","r+").readlines()
    negemotes=open("../data/neg-emote","r+").readlines()
    #initialize feeling indices
    feelindex=[]
    feelindex.append(feels[0].split(":")[0])
    curfeel=feels[0].split(":")[0]
    for feel in feels:
        if feel=="----":
            continue
        if not feel.split(":")[0] == curfeel:
            curfeel=feel.split(":")[0]
            feelindex.append(feel.split(":")[0])
    for item in bags:
        feats.write(item[0:10]+" ")
        bag=item[12:]
        bag=bag.strip("[]")
        bagsplit=bag.split(",")
        #print bagsplit
        vec=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for spl in bagsplit:
            spl=spl.strip("' ").lower()
            #check to see if it's an affective word
            for feel in feels:
                if feel=="----\n":
                    continue
                #print feel.split(":")
                if spl.count(feel.split(":")[1].strip()) > 0 or spl.count(feel.split(":")[0]) > 0:
                    vec[feelindex.index(feel.split(":")[0])]+=1
                    break
            #check for repeated letters      
            rep=0
            curlet="?"
            for letter in spl:
                if letter==curlet and not letter == "!" or letter == "?":
                    rep+=1
                else:
                    rep=0
                    curlet=letter
                if rep==2:
                    vec[17]+=1
                    break
            #check to see if it's an emote        
            for emote in posemotes:
                if emote.count(spl) > 0:
                    vec[18]+=1
            for emote in negemotes:
                if emote.count(spl) > 0:
                    vec[19]+=1
            #check to see if it's punctuation
            if spl.count("!!") > 0 or spl.count("??") > 0:
                vec[20]+=1
            #check to see if it's a swearword
            for swear in swearlex:
                #print swear
                if spl.count(swear.strip()) > 0:
                    vec[21]+=1
                    break
        feats.write(str(vec)+"\n")


if __name__=="__main__":
    main()
