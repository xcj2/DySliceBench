import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

N=II()
cnt = 0
for i in range(1,10):
    for i_keta in range(6):
        for j in range(1,10):
            for j_keta in range(6):
                A = i if i_keta == 0 else int(str(i) + ("0"*(i_keta-1)) + str(j))
                B = j if j_keta == 0 else int(str(j) + ("0"*(j_keta-1)) + str(i))
                if A <= N and B <=N:
                    if i_keta == 0 or j_keta == 0:

                        patA = 0
                        if i_keta:
                            if (i+1)*(10**i_keta) <= N:
                                patA = 10**(i_keta-1)
                            else:
                                for k in range(10000):
                                    if A+k*10 <= N:
                                        patA += 1
                                    else:
                                        break
                        else:
                            patA=1

                        patB = 0
                        if j_keta:
                            if (j+1)*(10**j_keta) <= N:
                                patB = 10**(j_keta-1)
                            else:
                                for k in range(10000):
                                    if B+k*10 <= N:
                                        patB += 1
                                    else:
                                        break
                        else:
                            patB = 1


                        if i == j:
                            # print(A,B,patA*patB)
                            cnt += patA*patB
                    else:
                        patA = 0
                        if (i+1)*(10**i_keta) <= N:
                            patA = 10**(i_keta-1)
                        else:
                            for k in range(10000):
                                if A+k*10 <= N:
                                    patA += 1
                                else:
                                    break

                        patB = 0
                        if (j+1)*(10**j_keta) <= N:
                            patB = 10**(j_keta-1)
                        else:
                            for k in range(10000):
                                if B+k*10 <= N:
                                    patB += 1
                                else:
                                    break
                        cnt += patA*patB
                        # print(A,B,patA*patB)

print(cnt)
