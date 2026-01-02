import sys
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


## エラトステネス のふるい(n以下の素数全列挙)
# O(NloglogN)
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [i for i in range(1, n+1) if is_prime[i-1]]
    return table,is_prime

def main():
    Q = INT()
    N = 10**5
    table,is_prime = sieve(N)
    is_like_number = [0]*(N+1)
    from itertools import accumulate
    for prime in table:
        if prime == 2:
            continue
        if is_prime[(prime+1)//2-1]:
            is_like_number[prime] = 1
    accum_like_number = list(accumulate(is_like_number))
    for _ in range(Q):
        l,r = MAP()
        print(accum_like_number[r]-accum_like_number[l-1])

    return

if __name__ == '__main__':
    main()
