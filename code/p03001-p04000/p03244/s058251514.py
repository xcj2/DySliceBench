import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def split_even_or_odd(vv, n, start):
    res = {}
    for i in range(start,n,2):
        v = vv[i]
        if not v in res.keys(): res[v] = 1
        else: res[v] += 1
    return res

def find_fs(target):
    maxk1 = maxv1 = 0
    for k, v in target.items():
        if maxv1 < v:
            maxk1, maxv1 = k, v
    maxk2 = maxv2 = 0
    for k, v in target.items():
        if maxv2 < v and maxk1 != k:
            maxk2, maxv2 = k, v
    return (maxk1, maxv1), (maxk2, maxv2)

def main():
    n = II()
    vv = MII()
    ee = split_even_or_odd(vv, n, 0)
    oo = split_even_or_odd(vv, n, 1)

    e1kv, e2kv = find_fs(ee)
    o1kv, o2kv = find_fs(oo)

    minv = 10**5
    if e1kv[0] != o1kv[0]:
        minv = min(minv, n - (e1kv[1] + o1kv[1]))
    else:
        minv = min(minv, n - (e1kv[1] + o2kv[1]))
        minv = min(minv, n - (e2kv[1] + o1kv[1]))
    print(minv)

if __name__ == '__main__':
    main()
