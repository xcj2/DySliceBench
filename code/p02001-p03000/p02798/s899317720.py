import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

#インデックス付きソート
#(index,value)の順に格納
from operator import itemgetter
def index_sort(A):
    return sorted(enumerate(A),key=itemgetter(1))

ceil = math.ceil
floor = math.floor

N = I()
A = III()
B = III()

ans = float('inf')
for i in range(1<<N):
    bits = format(i,'b').zfill(N)
    last_odd_val = []
    last_even_val = []
    for j,b in enumerate(bits):
        if j%2==0:
            if b=='0':
                last_even_val.append([A[j],j])
            else:
                last_odd_val.append([B[j],j])
        else:
            if b=='0':
                last_odd_val.append([A[j],j])
            else:
                last_even_val.append([B[j],j])

    if len(last_even_val)!=ceil(N/2):
        continue

    s_odd = sorted(last_odd_val,key=lambda x:(x[0],x[1]))
    s_even = sorted(last_even_val,key=lambda x:(x[0],x[1]))
    flag = False
    eps = 10**(-2)
    for j in range(N//2):
        if floor(s_even[j][0])>floor(s_odd[j][0]):
            flag = True
            break
        if floor(s_even[j][0])==floor(s_odd[j][0]):
            s_odd[j][0] = s_even[j][0] + eps
        if len(s_even)>j+1:
            if floor(s_odd[j][0])>floor(s_even[j+1][0]):
                flag = True
                break
            if floor(s_odd[j][0])==floor(s_even[j+1][0]):
                s_even[j+1][0] = s_odd[j][0] + eps

    if flag:
        continue

    val = [0.0]*N
    for s in s_even:
        val[s[1]] = s[0]
    for s in s_odd:
        val[s[1]] = s[0]

    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if val[i]>val[j]:
                count += 1
    
    if count<ans:
        ans = count

if ans == float('inf'):
    ans = -1
print(ans)