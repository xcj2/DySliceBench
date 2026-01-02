from sys import stdin
#from collections import deque
#from math import ceil


def ii(): return int(stdin.readline())


def fi(): return float(stdin.readline())


def mi(): return map(int, stdin.readline().split())


def fmi(): return map(float, stdin.readline().split())


def li(): return list(mi())


def lsi():
    x=list(stdin.readline())
    x.pop()
    return x


def si(): return stdin.readline()


def sieve(x):
    a=[True]*(x+1)
    sq=floor(sqrt(x))
    for i in range(3, sq+1, 2):
        if a[i]:
            for j in range(i*i, x+1, i):
                a[j]=False
    if x>1:
        p=[2]
    else:
        p=[]
    for i in range(3, x+1, 2):
        if a[i]:
            p.append(i)
    return p
#vowel={'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
pow=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416, 35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624, 2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968, 72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488, 1152921504606846976, 2305843009213693952, 4611686018427387904, 9223372036854775808]
############# CODE STARTS HERE #############
n=ii()
p=0
for i in pow:
    if i>n:
        break
    p+=i
print(p)