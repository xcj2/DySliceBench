def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0]*n]

    def det(x, y, z):
        a = [x[0]-y[0], x[1]-y[1]]
        b = [z[0]-x[0], z[1]-x[1]]
        return a[0]*b[1]-a[1]*b[0]

    def convex_hull(ab):
        q, k = [], 0
        xy = sorted(ab)  # ここをいじることで初期位置を変えられる。
        for i in range(n):
            while k > 1 and det(q[k-1], q[k-2], xy[i]) <= 0:
                k -= 1
                q.pop()
            q.append(xy[i])
            k += 1
        t = k
        for i in range(n-2, -1, -1):
            while k > t and det(q[k-1], q[k-2], xy[i]) <= 0:
                k -= 1
                q.pop()
            q.append(xy[i])
            k += 1
        return q[:k-1]

    ans = convex_hull(ab)
    l = len(ans)
    d = dict()
    from math import acos
    from math import pi
    if l == 2:
        for a, b in ans:
            d[(a, b)] = 0.5
    else:
        b = 0
        ans += ans
        for i in range(l):
            a1 = ans[i][0]-ans[i-1][0]
            b1 = ans[i][1]-ans[i-1][1]
            a2 = ans[i+1][0]-ans[i][0]
            b2 = ans[i+1][1]-ans[i][1]
            a = acos((a1*a2+b1*b2)/((a1**2+b1**2)*(a2**2+b2**2))**0.5)
            d[tuple(ans[i])] = a/2/pi
    for a, b in ab:
        if (a, b) in d:
            print(d[(a, b)])
        else:
            print(0)


main()