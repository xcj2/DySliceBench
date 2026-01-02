def iread():
    return int(input())


def sread():
    return input()


def aread_int():
    tmp = input().split()
    ret = [int(i) for i in tmp]
    return ret


def aread_str():
    return input().split()


def fst(t):
    return t[0]


def snd(t):
    return t[1]


def thd(t):
    return t[2]


if __name__ == '__main__':
    n, m = map(int, input().split())
    l = []
    ans = []
    for i in range(m):
        p, y = map(int, input().split())
        l.append((p, y, i))

    l = sorted(l)
    end = 0
    for i in range(n):
        begin = end
        while end < len(l) and fst(l[end]) == i + 1:
            end += 1
        town = l[begin:end]
        sorted(town, key=lambda x: snd(x))
        tmp = 1
        for e in town:
            ans.append((fst(e), tmp, thd(e)))
            tmp += 1

    ans = sorted(ans, key=lambda x : thd(x))
    for e in ans :
        birth = str(fst(e))
        rate = str(snd(e))
        print(birth.zfill(6) + rate.zfill(6))