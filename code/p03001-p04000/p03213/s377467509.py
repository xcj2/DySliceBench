
import math


def prime_factorization(x):
    if x == 1:
        return {1: 1}

    notprime = {}
    pf = {}
    for y in range(2, math.ceil(math.sqrt(x)) + 1):
        if y not in notprime.keys():
            if x % y == 0:
                pf[y] = 0
                while x % y == 0:
                    x //= y
                    pf[y] += 1
            
            coef = 2
            while coef * y < x:
                notprime[coef * y] = True
                coef += 1
    if x > 1:
        pf[x] = 1    
    return pf


def submit():
    n = int(input())

    #　階乗の素因数分解を求める
    pf_all = {}
    for x in range(2, n + 1):
        pf = prime_factorization(x)
        for k, v in pf.items():
            if k not in pf_all.keys():
                pf_all[k] = v
            else:
                pf_all[k] += v

    pf_cand = [v for k, v in pf_all.items() if v > 1]
    pf_cand.sort()
    possible_divisors = [1, 3, 5, 15, 25, 75]
    
    def dfs(curr, rest, cnt):
        if curr > 75:
            return cnt
        if not rest:
            if curr == 75:
                return cnt + 1
            else:
                return cnt
        
        l = rest[-1]
        new_rest = rest[:-1]
        for p in possible_divisors:
            if p - 1 <= l:
                cnt = dfs(curr * p, new_rest, cnt)
            else:
                break
        return cnt
            
    print(dfs(1, pf_cand, 0))


if __name__ == "__main__":
    submit()
