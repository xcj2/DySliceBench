#template
from collections import Counter
def inputlist(): return [int(k) for k in input().split()]
def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)
#template
ans = 10**18
N,A,B,C = inputlist()
l = [0]*N
for i in range(N):
    l[i] = int(input())

n = 4**N

def count(li,n):
    co = 0
    co += (len(li)-1)*10
    co += abs(sum(li) - n)
    return co

for i in range(n+1):
    k = base10to(i,4)
    if len(k) < N:
        d = N-len(k)
        for j in range(d):
            k = '0'+k
    c = Counter(list(k))
    if c['1'] < 1 or c['2'] < 1 or c['3'] < 1:
        continue
    ans_k = 0
    la = []
    lb = []
    lc = []
    for j in range(N):
        if k[j] == '1':
            la.append(l[j])
        if k[j] == '2':
            lb.append(l[j])
        if k[j] == '3':
            lc.append(l[j])
    ans_k += count(la,A) + count(lb,B) + count(lc,C)
    ans = min(ans,ans_k)
print(ans)
