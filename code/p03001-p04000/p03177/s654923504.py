def power(a, k):
    N = len(a)
    r = [[1 if i==j else 0 for i in range(N)] for j in range(N)]
    while k:
        if k & 1:
            r = mul(r, a)
        k >>= 1
        a = mul(a, a)
    return r
def mul(a, b):
    return [[sum(ay * by for ay, by in zip(ax, bx)) % (10**9 + 7) for bx in zip(*b)] for ax in a]
def main():
    N, K = map(int, input().split())
    l = []
    for _ in range(N):
        l.append(list(map(int, input().split())))
    lt = [i for i in zip(*l)]
    return sum(mul([[1]*N], power(lt, K))[0])
    #return l
#print(main())
print(main() % (10**9 + 7))
