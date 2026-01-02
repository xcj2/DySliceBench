from heapq import heappush,heappop

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))


def runLength(in_str):
    kukan = 1
    start = 0
    ret = []
    for i in range(1,len(in_str)):
        if in_str[i-1]!=in_str[i]:
            ret.append([in_str[i-1],kukan,start])
            start = i
            kukan=0
        kukan+=1
    ret.append([in_str[-1],kukan,start])
    return ret

N, K = ints_raw()
S = input()
cts = []
ctree = {}

def main():
    global cts
    ans = 0
    kukan = 1
    start = 0
    if S[0]=="0":
        cts.append(["1",0,0])
    cts += runLength(S)
    if S[-1]=="0":
        cts.append(["1",0, N-1])
    if K*2+1 >= len(cts):
        return N
    buf = sum([cts[i][1] for i in range(K*2+1)])
    ans = buf
    for i in range(K*2+1,len(cts)):
        n_buf = buf-cts[i-(K*2+1)][1]+cts[i][1]
        if cts[i][0]=="1":
            ans =max(ans,n_buf)
        buf = n_buf
    return ans

print(main())

