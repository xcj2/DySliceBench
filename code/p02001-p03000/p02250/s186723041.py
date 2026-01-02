from collections import Counter
import time

def SL(S):
    t = ["S"]*len(S)
    for i in range(len(S)-2,-1,-1):
        if S[i] > S[i+1] or (S[i] == S[i+1] and t[i+1] == "L"):
            t[i] = "L"
    return t

def LMS(t):
    lms = [False]*len(t)
    for i in range(1,len(t)):
        if t[i-1] == "L" and t[i] == "S":
            lms[i] = True
    return lms

def Bucket(S):
    bucket = Counter(S)
    tmp = 0
    for i in sorted(bucket):
        bucket[i] = {"chead":tmp,"ctail":tmp+bucket[i]-1}
        tmp = bucket[i]["ctail"]+1
    return bucket

def STEP2(S,t,bucket,SA):
    for i in range(len(SA)):
        tmp = SA[i]-1
        if t[tmp] == "L" and tmp > -1:
            head = bucket[S[tmp]]["chead"]
            SA[head] = tmp
            bucket[S[tmp]]["chead"]+=1

def STEP3(S,t,SA):
    bucket = Bucket(S)
    for i in range(len(SA)-1,-1,-1):
        tmp = SA[i]-1
        if t[tmp] == "S" and tmp > -1:
            tail = bucket[S[tmp]]["ctail"]
            SA[tail] = tmp
            bucket[S[tmp]]["ctail"]-=1
        
def InducedSorting(S):
    l = len(S)
    t = SL(S)
    lms = LMS(t)
    bucket = Bucket(S)
    SA=[-1]*l
    P1 = [i for i in range(l) if lms[i]]
    #STEP1
    for i,j in enumerate(lms):
        if j:
            tail = bucket[S[i]]["ctail"]
            SA[tail] = i
            bucket[S[i]]["ctail"] -= 1
    #STEP2
    STEP2(S,t,bucket,SA)
    #STEP3
    STEP3(S,t,SA)
    #Construct S1 from pseudoSA
    prev = None
    Name = [None]*l
    name = 0
    S1 = []
    for i in SA:
        if lms[i]:
            if prev and not i == len(S)-1:
                j = 0
                while(True):
                    if not S[i+j] == S[prev+j] or not t[i+j] == t[prev+j]:
                        name+=1
                        break
                    if j>0 and lms[i+j]:
                        break
                    j+=1
            Name[i] = name
            prev = i
    for i in Name:
        if not i == None:
            S1.append(i)
    #Construct SA1 from S1
    uniq = True
    dtmp = {}
    #for i in Counter(S1):
    #    if Counter(S1)[i] > 1:
    #        uniq = False
    #        break
    for i in S1:
        if i in dtmp:
            uniq = False
            break
        else:
            dtmp[i] = True
    
    if uniq:
        SA1 = [None]*len(S1)
        for i,j in enumerate(S1):
            SA1[j] = i
    else:
        SA1 = InducedSorting(S1)
    
    #Inducing SA from SA1 STEP1
    bucket = Bucket(S)
    SA=[-1]*l
    for i in SA1[::-1]:
        p = P1[i]
        tail = bucket[S[p]]["ctail"]
        SA[tail] = p
        bucket[S[p]]["ctail"] -= 1
    #Inducing SA from SA1 STEP2
    STEP2(S,t,bucket,SA)
    #Inducing SA from SA1 STEP3
    STEP3(S,t,SA)
    return SA

def contain(T,sa,P):
    a = 0
    b = len(T)
    while(b-a > 1):
        c = (a+b)//2
        if T[sa[c]:sa[c]+len(P)] < P:
            a = c
        else:
            b = c
    return P == T[sa[b]:sa[b]+len(P)]

T = input()
Q = int(input())
P = [input() for _ in range(Q)]
SA = InducedSorting(T+"$")
for i in P:
    if contain(T,SA,i):
        print(1)
    else:
        print(0)
