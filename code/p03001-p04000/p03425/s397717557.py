def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def C():
    N = ii()
    d = {'M': 0, 'A':0, 'R':0,'C':0,'H':0}
    for _ in range(N):
        s = input()
        if s[0] in d.keys():
            d[s[0]] += 1

    from itertools import combinations

    ans = 0
    for e1, e2, e3 in combinations(d.keys(), 3):
        ans += d[e1] * d[e2] * d[e3]

    print(ans)

if __name__ == '__main__':
    C()

