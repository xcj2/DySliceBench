import sys
import numpy as np
input = sys.stdin.readline

def factorization(num):
    import math
    # 因数分解した結果をタプルのリストで返す
    # [(prime, count), ...]
    MAX_PRIME = int(math.sqrt(num)) + 1
    primes = []
    is_prime = [True] * (MAX_PRIME+1)
    for i in range(2, MAX_PRIME+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, MAX_PRIME+1, i):
                is_prime[j] = False
    insu = []
    tmp = num
    max_count = 0
    for i in range(len(primes)):
        count = 0
        while tmp%primes[i] == 0:
            tmp //= primes[i]
            count += 1
        if count > 0:
            insu.append((primes[i], count))
            max_count = max(max_count, count)
        if tmp == 1:
            break
    if tmp != 1:
        insu.append((tmp, 1))
    return insu

def main():
    N = int(input())

    dic = {}
    for i in range(1, N+1):
        insu = factorization(i)
        for p, count in insu:
            if p in dic:
                dic[p] += count
            else:
                dic[p] = count
    dic = np.array(sorted(dic.values()))
    
    def cc(num):# num-1以上の要素の個数
        return np.count_nonzero(dic >= num-1)
    
    print(cc(75) + cc(25) * (cc(3) - 1) + cc(15) * (cc(5) - 1) + cc(5) * (cc(5) - 1) * (cc(3) - 2) // 2)


if __name__ == "__main__":
    main()