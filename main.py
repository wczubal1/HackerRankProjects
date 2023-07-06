# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math
import os
import random
import re
import sys
import itertools
from Combinations import *
import time

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def importdata(file):
    list_ = open(file).read().split()
    return list_


def test2(inp, k):
    combo2=itertools.combinations(inp, 2)
    combination= [t for t in combo2 if (sum(t) % k != 0)]
    if len(combination)<math.comb(len(inp),2):
        return 0
    return 1

def cleanup(combo,notgood):
    temp = []
    for t in range(len(combo)):
        temp.append(set(notgood).issubset(combo[t]))
    temp = [not elem for elem in temp]
    combo = list(itertools.compress(combo, temp))
    return combo

def testmore(inp, j, k, failedpairs):
    combinations=list(itertools.combinations(s, j))
    #if len(failedpairs)>0:
        #combinations = cleanup(combinations, failedpairs)
        #combinations = [t for t in combinations for yy in failedpairs if (set(yy) | set(t)) != set(t)]
    i=0
    while i<len(combinations):
    #for combination in itertools.combinations(s, j):
        print(j)
        print(combinations[i])
        y = test2(combinations[i], k)
        if y == 1:
            return 1
        else:
            #failedpairs.append(y)
            #failedpairs=y
            #combinations=[(t) for t in combinations for yy in failedpairs if (set(yy) | set(t)) != set(t)]
            #combinations=[(t) for t in combinations if (set(y) | set(t)) != set(t)]
            #[t for t in combinations if (set(y).issubset(t)) in combinations]
            #combinations=cleanup(combinations, y)
            #print(456)
            i=i+1

    return 0


def nonDivisibleSubset(k, s):
    # Write your code here
    print(len(s))
    if len(s) == 1:
        return 1
    j = 6
    failedpairs=[]
    while j <= len(s):
        print(j)
        if testmore(s, j, k, failedpairs) == 0:
            j = j - 1
            break
        if j == len(s):
            j = j
            break
        else:
            j = j + 1
    return j

def test3(inp, k):
    combo2=itertools.combinations(inp, 2)
    return [t for t in combo2 if (sum(t) % k == 0)]

def test4(inp, k):
    s_fup=[]
    j=0
    while j<len(inp)-1:
        jj=j+1
        while jj<len(inp):
            if (inp[j]+inp[jj]) % k ==0:
                s_fup.append((inp[j],inp[jj]))
                jj = jj + 1
            jj=jj+1
        j=j+1
    return s_fup

def nonDivisibleSubset2(k, s):
    s_fup= test4(s,k)
    if len(s_fup) == 0:
        return len(s)
    while len(s_fup) > 0:

            s_fup = test4(s, k)
            if len(s_fup) == 0:
                return len(s)
            flat_list = [item for sublist in s_fup for item in sublist]
            s.remove(max(flat_list, key=flat_list.count))

def nonDivisibleSubset3(k, s):
    #combinations = list(itertools.combinations(s, len(s)))
    s_fup = []
    j = 0
    while j < len(s) - 1:
        jj = j + 1
        while jj < len(s):
            if (s[j] + s[jj]) % k == 0:
                s_fup.append((s[j], s[jj]))
                jj = jj + 1
            jj = jj + 1
        j = j + 1
    if len(s_fup) == 0:
        return len(s)
    flat_list = [item for sublist in s_fup for item in sublist]
    s.remove(max(flat_list, key=flat_list.count))
    while len(s_fup) > 0:
        #if len(s_fup) == len(s):
        #    return len(s)
        #else:
        s_fup = []
        j = 0
        while j < len(s) - 1:
            jj = j + 1
            while jj < len(s):
                if (s[j] + s[jj]) % k == 0:
                    s_fup.append((s[j], s[jj]))
                    jj = jj + 1
                jj = jj + 1
            j = j + 1
        if len(s_fup) == 0:
            return len(s)
        flat_list = [item for sublist in s_fup for item in sublist]
        s.remove(max(flat_list, key=flat_list.count))
        print(2)
        #if len(combinations_fixed)<len(combinations):

def nonDivisibleSubset4(k, s):
    #s[:] = [x % k for x in s]
    s_fup = []
    j = 0
    while j < len(s) - 1:
        jj = j + 1
        while jj < len(s):
            if (s[j] + s[jj]) % k == 0:
                s_fup.append((s[j], s[jj]))
                jj = jj + 1
            else:
                jj = jj + 1
        j = j + 1
    if len(s_fup) == 0:
        return len(s)
    k=len(s_fup)
    print(s_fup)
    l=0
    while k>0:
        flat_list = [item for sublist in s_fup for item in sublist]
        tempr=(max(flat_list, key=flat_list.count),)
        print(tempr[0])
        s_fup = list(filter(lambda x: set(x) | set(tempr) != set(x), s_fup))
        print(s_fup)
        k = len(s_fup)
        l=l+s.count(tempr[0])
        print(s.count(tempr[0]))
    return len(s)-l

def nonDivisibleSubset5(k, s):
    s[:] = [x % k for x in s]
    zero_cnt=0
    if s.count(0)>0:
        s = list(filter(lambda x: x != 0, s))
        zero_cnt=1
    mltp_cnt=len(s)
    s = list(filter(lambda x: 2*x != k, s))
    if mltp_cnt > len(s):
        s.append(k/2)
    print(s)
    s_unq = list(set(s))
    print(s_unq)
    j = 0
    while j < len(s_unq) - 1:
        jj = j + 1
        while jj < len(s_unq):
            if (s_unq[j] + s_unq[jj]) % k == 0:
                if s.count(s_unq[j]) <= s.count(s_unq[jj]):
                    s = list(filter(lambda x: x != s_unq[j], s))
                else:
                    s = list(filter(lambda x: x != s_unq[jj], s))
                jj = jj + 1
            else:
                jj = jj + 1
        j = j + 1
    print(s)
    return len(s)+zero_cnt

if __name__ == '__main__':
    start_time = time.time()
    #s=importdata(r'C:\Users\witol\Documents\Computing\HackerRank\input09.txt')
    #k=int(s[1])
    #del s[0:2]
    #s=list(map(int, s))

    k = 4
    #k=3
    #k=7

    #temp = '61197933 56459859 319018589 271720536 358582070 849720202 481165658 675266245 541667092 615618805 129027583 755570852 437001718 86763458 791564527 163795318 981341013 516958303 592324531 611671866 157795445 718701842 773810960 72800260 281252802 404319361 757224413 682600363 606641861 986674925 176725535 256166138 827035972 124896145 37969090 136814243 274957936 980688849 293456190 141209943 346065260 550594766 132159011 491368651 3772767 131852400 633124868 148168785 339205816 705527969 551343090 824338597 241776176 286091680 919941899 728704934 37548669 513249437 888944501 239457900 977532594 140391002 260004333 911069927 586821751 113740158 370372870 97014913 28011421 489017248 492953261 73530695 27277034 570013262 81306939 519086053 993680429 599609256 639477062 677313848 950497430 672417749 266140123 601572332 273157042 777834449 123586826'
    #temp='1 2 7 4'
    temp='1 2 3 4 5 6 7 8 9 10'
    #temp='278 576 496 727 410 124 338 149 209 702 282 718 771 575 436'
    #temp='576 496 727 410 338 149 209 702 282 718 575 436'
    s=list(map(int, temp.split(' ')))

    result = nonDivisibleSubset5(k, s)

    #result=combinations('ABCD',2)
    print(result)
    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
