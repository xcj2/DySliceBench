import math
import sys
sys.setrecursionlimit(10000000)
Q = int(input())
l_r = [list(map(int, input().split())) for _ in range(Q)]

prime = []
def isprime(n):
    if n in prime:
        return True
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True


def like(x):
    if isprime(x) and isprime((x+1)//2):
        return True
    
    return False

x_dict = {1:0}
def count_like(x):
    if x in x_dict:
        return x_dict[x]
    x_dict[x] = count_like(x-1) + like(x)
    return x_dict[x]

for i in range(Q):
    print(count_like(l_r[i][1]) - count_like(l_r[i][0]) + int(like(l_r[i][0])))
