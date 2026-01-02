from sys import stdin
##  input functions for me
def ria(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##

## main ##
N = ri()
S = [""] * N
for i in range(N):
    S[i] = rs()

di = dict()
for s in S:
    if not s in di: di[s] = 0
    di[s] += 1

ma = 0
for s in di:
    ma = max(ma, di[s])

l = []
for s in di:
    if di[s] == ma: l.append(s)

l.sort()
print("\n".join(l))


