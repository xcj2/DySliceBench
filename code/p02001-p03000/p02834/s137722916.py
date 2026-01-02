def dps_rec(no, fno, d, hen, D, MD, P):
    D[no] = d
    P[no] = fno
    maxd = d
    for h in hen[no]:
        if h == fno:
            continue
        maxd = max(maxd, dps_rec(h, no, d + 1, hen, D, MD, P))
    MD[no] = maxd
    return maxd

def dps_stc(no, fno, d, hen, D):
    stack = [(no, fno, d)]
    while not stack == []:
        t = stack.pop()
        D[t[0]] = t[2]
        for h in hen[t[0]]:
            if h == t[1]:
                continue
            stack.append((h, t[0], t[2] + 1))

def main():
    N, u, v = map(int, input().split())
    hen = {}
    for i in range(N - 1):
        A, B = map(int, input().split())
        if A in hen.keys():
            hen[A].append(B)
        else:
            hen[A] = [B]
        if B in hen.keys():
            hen[B].append(A)
        else:
            hen[B] = [A]
    DEPTH_A = [-1 for i in range(N + 1)]
    DEPTH_T = [-1 for i in range(N + 1)]
    dps_stc(v, -1, 0, hen, DEPTH_A)
    dps_stc(u, -1, 0, hen, DEPTH_T)
    ans = 0
    for a, t in zip(DEPTH_A, DEPTH_T):
        if a > t:
            ans = max(ans, a - 1)

    print(ans)


if __name__ == '__main__':
    main()
