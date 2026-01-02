def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a

def nCr(n,r):
    if r > n:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)

def nC2(n):
    if n < 2:
        return 0
    else:
        return n * (n-1) // 2


####
N = int(input())
sorted_dic = {}
for i in range(N):
    s = "".join(sorted(input()))
    v = 0
    if s in sorted_dic:
        v = sorted_dic[s]
    sorted_dic[s] = v + 1

ans = 0
for k in sorted_dic:
    v = sorted_dic[k]
    #print(k,v,factorial(v),factorial(2), factorial(v - 2), nCr(v, 2))
    ans = ans + nC2(v)

print(ans)