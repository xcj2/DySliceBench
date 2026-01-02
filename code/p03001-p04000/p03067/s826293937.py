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

A,B,C = ints_raw()

def main():

    if (A < C and C <B) or (A>C and C>B):
        return "Yes"
    else:
        return "No"

print(main())

