import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

def main():
    N, M = mi()
    A = sorted(li())

    '''
    for j in range(M):
        b, c = mi()
        ind = min(bisect.bisect_left(A, c), b)
        A = sorted([c]*ind + A[ind:])
    
    print(sum(A))
    '''
    ab = li2(M)
    ab.sort(key=lambda x: x[1], reverse=True)
    c_list = []
    l = 0
    for b, c in ab:
        if l + b > N:
            c_list += [c]*(N-l)
            l = N
        else:
            c_list += [c]*b
            l += b
        if l == N:
            break
    ans = sum(sorted(A+c_list, reverse=True)[:N])
    print(ans)

if __name__ == "__main__":
    main()