from sys import stdin, stdout
import math
import bisect
import datetime
from collections import defaultdict
import random

def bl_solve(a):
    ans = []
    for k in range(2, a + 1):
        tmp = a
        while tmp > 0:
            if tmp % k == 0:
                tmp = tmp // k
            else:
                tmp -= k
            if tmp == 1:
                ans.append(k)
                break
    return ans

def bl_solve2(a):
    if a == 2:
        ans = 1
    else:
        ans = 2
    for k in range(2, int(math.sqrt(a))+1):
        tmp = a
        while tmp >= k:
            if tmp % k == 0:
                tmp = tmp // k
            else:
                tmp %= k
        if tmp == 1:
            ans+=1
        if (a - 1) % k == 0 and k != math.sqrt(n - 1):
            ans+=1
    return ans

def fj(a):
    arr = defaultdict(int)
    i = 2
    while i <= math.sqrt(a):
        while a % i == 0:
            a //= i
            arr[i] += 1
        i += 1
    if a != 1:
        arr[a] += 1
    ans = 1
    for key, value in arr.items():
        ans *= (value + 1)
    return ans-1

def solve(a):
    if a == 2:
        return 1
    ans = fj(a - 1)
    i = 2
    while True:
        tmp = round(a**(1 / i))
        if tmp ** i == a:
            ans += 1
        if tmp < 2:
            break
        i+=1
    return ans + 1
    

n = int(stdin.readline().strip())

ans = bl_solve2(n)
stdout.writelines(str(ans)+'\n')

# for n in range(2, 10000):
#     ans = bl_solve(n)
#     ans2 = bl_solve2(n)
#     if ans2 == len(ans):
#         print('True')
#     else:
#         print('False')
#         print(ans2,len(ans),ans)
#         input()
    # print(n, len(ans), ans)
    