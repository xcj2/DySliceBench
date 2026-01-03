# ABC 060
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

a,b,c = getIntList()
rm = a % b
rslt = 'NO'
for i in range(b+1):
    if a%b==c:
        rslt = 'YES'
        break
    a += rm
db(a)
print(rslt)
        