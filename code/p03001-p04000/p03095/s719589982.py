MOD = 10 ** 9 + 7

plist = [-1] * 65
def p(x):
    if plist[x] != -1:return plist[x]
    if x == 0:
        plist[x] = 1
        return 1
    if x % 2 == 0:
        plist[x] = p(x//2)*p(x//2)%MOD
        return plist[x]
    plist[x] = 2*(p(x//2)*p(x//2)%MOD)%MOD
    return plist[x]

def add(x,y):
    return (x+y) % MOD
def mul(x,y):
    return x*y % MOD

N = int(input())
S = input()

cnt = [0] * 26
for i in range(N):
    cnt[ord(S[i])-97] += 1

flag = True
for i in range(26):
    if cnt[i] > 1:
        flag = False

if flag:
     print(add(-1,p(N)))
else:
    ans = 1
    for i in range(26):
        ans = mul(ans,1+cnt[i])
    print(add(-1,ans))
    