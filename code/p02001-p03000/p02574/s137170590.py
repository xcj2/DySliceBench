import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    from collections import defaultdict
    def get_sieve_of_eratosthenes(n, D):
        limit = int(n ** 0.5) + 1
        cnt_list = [0] * (n + 1)
        for i in range(2, limit + 1):
            if cnt_list[i] == 0:
                k = n // i
                for j in range(1, k + 1):
                    s = i * j
                    if cnt_list[s] == 0:
                        D[s] = i
                        cnt_list[s] = 1
        for l in range(limit, n + 1):
            if cnt_list[l] == 0:
                D[l] = l
                cnt_list[l] = 1
        return D



    N = I()
    A = LI()
    D = defaultdict()
    max_a = max(A)
    num_list = [0] * (max_a + 1)
    if max_a == 1:
        print("pairwise coprime")
        exit()

    g = A[0]
    for a in A:
        g = math.gcd(g, a)
    if g > 1:
        print('not coprime')
        exit()

    A_ = set(A)
    A_.discard(1)
    if len(A_) >= 90000:
        print('setwise coprime')
        exit()

    D = get_sieve_of_eratosthenes(max_a, D)
    for a in A:
        P_list = defaultdict(int)
        while a != 1:
            x = D[a]
            P_list[x] += 1
            a //= x
        for key in P_list.keys():
            if num_list[key] != 0:
                print('setwise coprime')
                exit()
            num_list[key] = 1

    print('pairwise coprime')

if __name__ == "__main__":
    main()
