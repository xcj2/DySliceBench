import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


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

n,d,a = map(int, input().split())
xh = [None]*n
# h = [None]*n
for i in range(n):
    xh[i] = tuple(map(int, input().split()))
xh.sort()

bit = [0] * (n+1)
r = 0
val = 0
done = False
for l,(x,h) in enumerate(xh):
    bound = x+2*d
    while r<n and xh[r][0]<=bound:
        r += 1
    nokori = h + query(bit, l+1)
    if nokori>0:
#         print(nokori, a, l, r, bit)
        num = nokori//a + int(nokori%a!=0)
        val += num
        update(bit, l+1, -num*a)
        if r<n:
            update(bit, r+1, num*a)
print(val)