# ABC 084
# 基本
import math
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def getIntFromRows(n): return [int(input()) for i in range(n)]
def getIntMat(n):
    mat = []
    for i in range(n): mat.append(getIntList())
    return mat

def zeros(n): return [0 for i in range(n)]
def zeros2(n, m): return [[0 for i in range(m)] for j in range(n)]
N1097 = 10**9 + 7 
debug = True
def db(x): 
    if debug: print(x)

debug = False
n = getInt()
c, s, f = zeros(n-1), zeros(n-1), zeros(n-1)
for i in range(n-1):
    c[i], s[i], f[i] = getIntList()
db((c,s,f))
for i in range(n-1):
    arriv = 0
    dept = s[i]
    for j in range(i+1, n-1):
        arriv = dept + c[j-1]
        dept = (max(arriv, s[j])+f[j]-1) // f[j] * f[j]
        db((arriv, dept))
    arriv = dept + c[n-2]
    print(arriv)
print(0)

