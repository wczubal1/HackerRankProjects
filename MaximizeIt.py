import math

def importdata(file):
    list_ = open(file).read().split()
    return list_
def MaximizeIt(x,m):
    #del x[0]
    return max([(int(i)**2) % m for i in x[1::]])

def MaximizeIt2(k,m,x):
    jj=[0] * len(x)
    z=0
    r=len(x)-2
    v=len(x)-1
    k=0
    while r + 1:
        while jj[r]<len(x[r]):
            while jj[v]<len(x[v]):
                while z < len(x):
                        print("z ",z,"jj[z]", jj[z], "r ",r, "v ",v)
                        print(int(x[z][jj[z]]))
                        z += 1
                print("         ")
                z=0
                jj[v] += 1
            jj[v]=0
            #r -= 1
            jj[r] += 1
            #v -= 1
            # jj[v] += 1
            # print("v ", v, "r ",r)
        jj[r] = 0
        r -= 1
        jj[r] += 1
        #v = len(x)-1

def RunLast(m,x,jj):
    z = 0
    MaxIt=0
    MaxItIs=[]
    while z < len(x):
        #print(int(x[z][jj[z]]))
        MaxIt += int(x[z][jj[z]]) ** 2
        MaxItIs.append(int(x[z][jj[z]]))
        z += 1
    #print("         ")
    MaxItIs.append(MaxIt % m)
    return MaxItIs

def MaximizeIt3(k,m,x):
    jj=[0] * len(x)
    z=0
    n=0
    nmax=[]
    r=len(x)-2
    v=len(x)-1
    k=0

    while v-1:
        while jj[v]<len(x[v]):
            nel=RunLast(m, x, jj)
            if nel[-1]>n:
                n=nel[-1]
                nmax=nel
            jj[v] += 1
            k+=1
        # jj[v]=0
        # v -= 1
        if jj[0] == len(x[0]) - 1 & m==0 :
            #print("Counter ", k)
            v = len(x) - 1
            m+=1
            continue
        while jj[v]>=len(x[v])-1:
            jj[v] = 0
            v-=1
        if v<0:
            print("Counter ", k, "MaximizeIt", n, "nmax ", nmax)
            break
        jj[v]+=1
        v=len(x)-1
        # if jj[v]<len(x[v])-1:
        #     jj[v] += 1
        #     v+=1
        # else:
        #     jj[v] = 0
        #     v-=1
        #     jj[v]+=1
        #     v=len(x)-1

        # print("v ", v, "r ",r)


def sublists(s):
    #creates list that holds lists as subs and deletes first obs
    subs = []
    while s:
        subs.append(s[1:int(s[0]) + 1])
        del s[0:int(s[0])+1]
    return subs


if __name__ == '__main__':

    s = importdata(r'D:\Witold\Documents\Computing\HackerRank\MaximizeIt\input3.txt')
    k = int(s[0])
    s = s[1:]
    m = int(s[0])
    s = s[1:]

    subS=[]
    subS= sublists(s)
    MaximizeIt3(k,m,subS)
    print(subS)

    # maxit = []
    # while s:
    #     z = s[0:int(s[0])+1]
    #     maxit.append(MaximizeIt(z,m))
    #     print(MaximizeIt(z,m))
    #     del s[0:int(s[0])+1]
    # print(sum(maxit))
