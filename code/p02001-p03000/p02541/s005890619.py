import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
def factor(n, m=None):
    # mを与えると、高々その素因数まで見て、残りは分解せずにそのまま出力する
    arr = {}
    temp = n
    M = int(-(-n**0.5//1))+1
    if m is not None:
        M = min(m+1, M)
    for i in range(2, M):
        if i>temp:
            break
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if not arr:
        arr[n] = 1

    return arr
n *= 2
f = factor(n)
# print(f)
from itertools import product
ans = n-1
def gcd2(a, b):
    """a*x + b*y = gcd(a,b)なるx,yも求める
    """
    l = []
    while b:
        l.append(divmod(a,b))
        a, b = b, a%b
    x, y = 1, 0
    for aa,bb in l[::-1]:
        x, y = y, x - aa*y
    return a, x, y
def sub(x,y):
    g,k,l = gcd2(x, -y)
    if g!=1:
        return None
    return abs(k*x)
for ks in product(*[range(2) for _ in f.values()]):
    val = 1
    val2 = 1
    for k,v in zip(ks, f.keys()):
        if k:
            val *= pow(v,f[v])
        else:
            val2 *= pow(v,f[v])
#     print(val*val2)
    if val==1 or val2==1:
        continue
    res = gcd2(val, -val2)
    if res is not None and abs(res[0])==1:
#         print(val,val2,res)
        ans = min(ans, abs(val*res[1]))
print(ans)