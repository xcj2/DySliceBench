def main():
    from sys import stdin
    input=stdin.readline
    from itertools import accumulate as ac

    n, k = map(int, input().split())
    a = [int(input())-k for _ in [0]*n]

    # bit木を作る
    bit = [0]*(n+2)

    # aにwを足す
    def add(a, w):
        x = a
        while x < n+2:
            # print(x)
            bit[x] += w
            x += x & (-x)

    # aまでの和をとる
    def sum_(a):
        ret = 0
        x = a
        while x > 0:
            ret += bit[x]
            x -= x & (-x)
        return ret

    aca = [0]+list(ac(a))
    aca = sorted([(i, j) for i, j in enumerate(aca)],
                 key=lambda x: -x[1])+[(0, 10**20)]
    temp = []
    temp2 = [aca[0][0]]
    for i in range(1, n+2):
        if aca[i][1] == aca[i-1][1]:
            temp2.append(aca[i][0])
        else:
            temp.append(temp2)
            temp2 = [aca[i][0]]
    ans = 0
    for temp2 in temp:
        l=len(temp2)
        ans += l*(l-1)//2
        for i in temp2:
            ans += sum_(n+1)-sum_(i)
        for i in temp2:
            add(i+1, 1)
    print(ans)


main()