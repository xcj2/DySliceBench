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

N = int_raw()
S= input()
K = int_raw()

def main():
    ans =""
    for c in S:
        if c==S[K-1]:
            ans+=c
        else:
            ans+="*"
    return ans


print(main())

