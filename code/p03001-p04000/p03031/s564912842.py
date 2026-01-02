def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, M = MI()
K, switch = [], []

for _ in range(M):
    k, *s = MI()
    K.append(k)
    switch.append(s)
    
p = LI()
ans = 0

for i in range(1 << N):
    on = [False] * N
    
    for j in range(N):
        if (i >> j) & 1:
            on[j] = True
    
    can = True
    
    for k in range(M):
        tmp = 0
        for s in switch[k]:
            tmp += on[s - 1]
            
        if tmp % 2 != p[k]:
            can = False
            break
    
    ans += can
    
print(ans)