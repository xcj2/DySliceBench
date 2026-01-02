#  --*-coding:utf-8-*--

import heapq

def sumOfDigits(n):
    a = 0

    while n > 0:
        a += n%10
        n //= 10

    return a


def f(n):
    while n%2 == 0:
        n //= 2

    while n%5 == 0:
        n //= 5

    vs = [None]*n
    qs = []
    x = sumOfDigits(n)

    for i in range(1, min(n, 10)):
        vs[i] = i
        heapq.heappush(qs, (i, i))

    while len(qs) > 0:
        _, q = heapq.heappop(qs)
        q2 = q*10
        v = vs[q]
        
        for i in range(0, min(x-v, 10)):
            q3 = (q2 + i)%n
            v2 = v + i
            v3 = vs[q3]

            if v3 == None or v2 < v3:
                vs[q3] = v2
                heapq.heappush(qs, (v2, q3))
                    
            if q3 == 0 and v2 < x:
                x = v2

    return x


def test():
    assert f(6) == 3
    assert f(41) == 5
    assert f(79992) == 36


def main():
    n = int(input())
    print(f(n))


if __name__ == '__main__':
    main()
