mod = 10**9 + 7
from collections import deque

def main():
    N, Q = iip(listed=False)

    ql = [0 for i in range(N)]
    ll = [[] for i in range(N)]

    for i in range(N-1):
        a, b = iip(True)
        ll[a-1].append(b-1)
        ll[b-1].append(a-1)

    for i in range(Q):
        p, x = iip(True)
        ql[p-1] += x

    que = deque([])
    que.append((0, None))

    result = [None for i in range(N)]
    while que:
        data = que.popleft()
        node = data[0]
        before_node = data[1]
        if before_node is None:
            before_num = 0
        else:
            before_num = result[before_node]

        result[node] = before_num + ql[node]

        for child in ll[node]:
            if child != before_node:
                que.append((child, node))


    print(" ".join([str(i) for i in result]))




#####################################################ライブラリ集ここから

def searchsorted(sorted_list, n, side):
    if side not in ["right", "left"]:
        raise Exception("sideはrightかleftで指定してください")

    l = 0
    r = len(sorted_list)

    while r-l > 1:
        x = (l+r)//2
        if sorted_list[x] > n:
            r = x
        elif sorted_list[x] < n:
            l = x
        else:
            if side == "left":
                r = x
            elif side == "right":
                l = x

    if side == "left":
        return r
    if side == "right":
        return l+1



def iip(listed):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
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


def conbination(n, r, mod, test=False):
    if n <=0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0
    if r == 1:
        return n
    ret = 1
    for i in range(n-r+1, n+1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r+1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    if test:
        #print(f"{n}C{r} = {ret}")
        pass
    return ret


def inv(n, mod):
    return power(n, mod-2)

def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p//2) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p-1)) % mod


if __name__ == "__main__":
    main()