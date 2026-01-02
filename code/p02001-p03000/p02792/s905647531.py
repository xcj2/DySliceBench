import math
import time


t = time.time()
def iip():
    ret = [int(i) for i in input().split()]
    if len(ret) == 1:
        return ret[0]
    return ret

def fkc(keta):
    return 10**keta

def pat_b(a, n):
    tail = a % 10

    if tail == 0:
        return 0

    head = int(str(a)[0])

    ret = 0
    if tail == head: #１桁解
        ret += 1

    if n >= tail*10+head: #２桁解は１通りあるかないか
        ret += 1

    for free_keta in range(1, 6): # 3桁以上解
        mincase = 10**(free_keta+1) * tail + head

        if n < mincase:
            break
        if n >= 10**(free_keta+1) + mincase + head - 10:
            ret += fkc(free_keta)
            continue
        else:
            ret += int(int(n-mincase)/10) + 1
    return ret

def main():
    n = iip()
    result = 0
    for i in range(n+1):
        result += pat_b(i, n)
    print(result)


main()