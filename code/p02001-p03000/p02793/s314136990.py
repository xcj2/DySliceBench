import sys
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
#リストの最小公倍数
def lcm(a):    
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x

def main():
    N = ir()
    A = lr()
    A.sort()
    if N == 1:
        print(1)
        exit()
    MOD = 10 ** 9 + 7
    l = []
    first = A[0]
    l = [x//gcd(x, first) for x in A[1:]]
    x = lcm(l) #B[0]
    answer = x%MOD

    for i in range(1, N):
        answer += first * x // A[i]

    print(answer%MOD)

if __name__ == '__main__':
    main()
