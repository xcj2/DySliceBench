#!/usr/bin/env python3
import sys
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    
    return table

def solve(N: int):
    from collections import Counter
    counter = Counter(prime_decomposition(math.factorial(N)))
    prime_counts = sorted(list(counter.values()),reverse=True)

    ## key個以上あるもののindex
    d = {74:[],24:[],14:[],4:[],2:[],1:[]}
    for i,count in enumerate(prime_counts):
        for key,_ in d.items():
            if count>=key:
                d[key].append(i)

    answer = 0
    ## ○**74の形のものが何個作れるか
    if d.get(74):
        answer += len(d[74])
    ## ○**24○*2の形のものが何個作れるか
    if d.get(24):
        answer += len(d[24])*(len(d[2])-1)

    ## ○**14○*4の形のものが何個作れるか
    if d.get(14):
        answer += len(d[14])*(len(d[4])-1)

    if len(d.get(4))>=2:
        answer += combinations_count(len(d[4]),2)*(len(d[2])-2)

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
