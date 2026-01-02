import math
import time
from collections import deque
from collections import defaultdict
from copy import deepcopy

mod = 10 ** 9 + 7
t = time.time()



def iip():
    ret = [int(i) for i in input().split()]
    if len(ret) == 1:
        return ret[0]
    return ret

def soinsuu_bunkai(n):
    ret = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            n //= i
            ret.append(i)
        if i > n:
            break
    if n != 1:
        ret.append(n)
    return ret


def main():
    A, B = iip()

    a = set(soinsuu_bunkai(A))
    b = set(soinsuu_bunkai(B))

    ans = 1 # 1の場合
    for aa in a:
        if aa in b:
            ans+=1

    print(ans)

main()