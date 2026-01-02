
def choose(D, c, s, d, last, depth, p):
    maxpoint = -999999
    maxnum = 0
    if depth > 0 and d < D:
        for i in range(26):
            point = p
            point += s[d][i]
            point += changepoint(c, d, i, last)
            nlast = []
            nlast.extend(last)
            nlast[i] = d
            z, point = choose(D, c, s, d+1, nlast, depth-1, point)
            if point > maxpoint:
                maxpoint = point
                maxnum = i
        return maxnum, maxpoint
    return 0, p


def changepoint(c, d, num, last):
    point = 0
    for j in range(26):
        if j != num:
            point -= c[j]*(d-last[j])
    return point


def main():
    D = int(input())
    c = list(map(int, input().split()))
    s = []
    last = [-1]*26
    for _ in range(D):
        s.append(list(map(int, input().split())))
    point = 0
    for i in range(D):
        num, point = choose(D, c, s, i, last, 1, 0)
        print(num+1)


main()
