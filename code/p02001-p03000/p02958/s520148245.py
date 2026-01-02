import sys
import math
INPUT = sys.stdin.readline
#入力関数
def SORO_INT(): return int(INPUT())
def MULT_INT_LIST(): return list(map(int, INPUT().split()))
def MULT_INT_MAP(): return map(int, INPUT().split())
def SORO_STRING(): return INPUT()
def MULT_STRING(): return INPUT().split()

N = SORO_INT()
A = MULT_INT_LIST()
X = sorted(A)
if A == X:
    print('YES')
    sys.exit()


i = 0
count=0
for i in range(N):
    if count>2:
        print('NO')
        sys.exit()
    
    if A[i]==i+1:
        count = count
    else:
        count+=1

print('YES')