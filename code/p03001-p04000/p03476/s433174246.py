import sys
import itertools
from itertools import accumulate
def main():
    import itertools
    def eratosthenes_sieve(n):
        table = [0] * (n + 1)
        prime_list = []
        for i in range(2, n + 1):
            if table[i] == 0:
                prime_list.append(i)
                for j in range(i + i, n + 1, i):
                    table[j] = 1
        return prime_list
        def inputs():return (int(x) for x in input().split())
    input = sys.stdin.readline
    def inputs():
        return (int(x) for x in input().split())
    M = 10**5
    prime_list=eratosthenes_sieve(M)
    kaku = set(prime_list)
    N = [0]*(M+1)
    for i in range(1,M+1,2):
        if i in kaku and ((i+1)/2 in kaku):
            N[i] =1 
    ans = list(accumulate(N))
    Q = int(input())
    for i in range(Q):
        l,r = inputs()
        print(ans[r]-ans[l-1])
main()