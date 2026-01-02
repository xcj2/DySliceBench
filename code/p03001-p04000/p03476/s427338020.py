import math
import itertools
import heapq
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque


# d = defaultdict(lambda: 0)
# setrecursionlimit(10**7)
# inf = float("inf")


##### stdin ####
def LM(t, r): return list(map(t, r))
def R(): return stdin.readline()
def RS(): return R().split()
def I(): return int(R())
def F(): return float(R())
def LI(): return LM(int,RS())
def LF(): return LM(float,RS())
def ONE_SL(): return list(input())
def ONE_IL(): return LM(int, ONE_SL())
def ALL_I(): return map(int, stdin)
def ALL_IL(): return LM(int,stdin)

##### tools #####
def ap(f): return f.append
def pll(li): print('\n'.join(LM(str,li)))
def pljoin(li, s): print(s.join(li))

##### main #####

def primes(max_number):
    """
    指定値未満の素数を取得するジェネレータ
    https://qiita.com/Mokkeee/items/93b6b7d59fa256aa1677
    """
    if max_number <= 2:
        raise StopIteration
    yield 2
    is_prime = [1] * max_number
    square_root_of_max = max_number ** 0.5
    for number in range(3, max_number, 2):
        if is_prime[number] is 0:
            continue
        yield number
        if number <= square_root_of_max:
            for multiple in range(number * 2, max_number, number):
                is_prime[multiple] = 0

def main():
	P = list(primes(10**5))
	P = [p for p in P[1:] if (p+1)//2 == P[bisect_left(P, (p+1)//2)]]
	n = I()

	for i in range(n):
		l, r = LI()
		a = bisect_left(P,l)
		b = bisect_right(P,r)
		print(b-a)


if __name__ == '__main__':
	main()