n = int(input())
k = int(input())



def choose(n, k):
    if k == 1:
        return n
    if k == 2:
        return n * (n-1) // 2
    if k == 3:
        return n * (n-1) * (n-2) // 6
    #print(f'choosing... k is {k}!')

def nonzerodigs(n):
    ss = list(map(int, list(str(n))))
    ss = [s for s in ss if s != 0]
    return len(ss)


def count(n, k):
    #print(f'count({n}, {k})')
    if k == 0:
        return 1

    if n < 1000:
        cnt = 0
        for i in range(1, n+1):
            if nonzerodigs(i) == k:
                cnt += 1

        return cnt

    ns = list(map(int, list(str(n))))
    d = len(ns)
    top3 = ns[0] * 100 + ns[1] * 10 + ns[2]
    cnt = 0
    for i in range(top3):
        nn = nonzerodigs(i)
        if nn > k:
            continue
        kk = k - nn
        if kk == 0:
            cnt += 1
        else:
            cnt += choose(d-3, kk) * (9**kk)

    nn = nonzerodigs(top3)
    if nn > k:
        return cnt
    elif nn == k:
        cnt += 1
        return cnt
    elif nn < k:
        kk = k - nn
        if kk > 2:
            print("ERROR")
            return -1
        nnn = int("".join(map(str, ns[3:])))
        return cnt + count(nnn, kk)

print(count(n,k))
