def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0]*n]

    def det(x, y, z):
        a = [x[0]-y[0], x[1]-y[1]]
        b = [z[0]-x[0], z[1]-x[1]]
        return a[0]*b[1]-a[1]*b[0]

    def convex_hull(xy):
        q, k = [], 0
        xy.sort(key=lambda x: (x[1], x[0]))
        for i in range(n):
            while k > 1 and det(q[k-1], q[k-2], xy[i]) < 0:
                k -= 1
                q.pop()
            q.append(xy[i])
            k += 1
        t = k
        for i in range(n-2, -1, -1):
            while k > t and det(q[k-1], q[k-2], xy[i]) < 0:
                k -= 1
                q.pop()
            q.append(xy[i])
            k += 1
        return q[:k-1]

    ans = convex_hull(ab)
    print(len(ans))
    for i, j in ans:
        print(i, j)


main()

