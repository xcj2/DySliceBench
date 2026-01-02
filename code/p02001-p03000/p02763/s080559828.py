import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



n = int(input())
s = input()
q = int(input())

### BIT 
def init(bit, values):
    for i,v in enumerate(values):
        update(bit,i,v)
#a1 ~ aiまでの和 O(logn)
def query(bit,i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i&(-i)
    return res

#ai += x(logN)
def update(bit,i,x):
    while i <= len(bit)-1:
        bit[i] += x
        i += i&(-i)
    return

l = [chr(v) for v in range(ord("a"), ord("z")+1)]
d = {c: [0] * (n+1) for c in l}
for i,c in enumerate(s):
    update(d[c], i+1, 1)
s = list(s)
ans = []
for i in range(q):
    v,i,c = input().split()
    if v=="1":
        i = int(i)-1
        if d[s[i]][i+1]>=1:
            update(d[s[i]], i+1, -1)
        update(d[c], i+1, 1)
        s[i] = c
    else:
        ll,rr = int(i),int(c)
        val = sum(query(d[c], rr) - query(d[c], ll-1) >= 1 for c in l)
        ans.append(val)
write("\n".join(map(str, ans)))