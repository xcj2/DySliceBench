import sys
input = sys.stdin.readline


def inpl():
    return list(map(int, input().split()))


def GetBase(t=0):
    ret = []
    last = -C * 2 - 1
    for i, s in enumerate(S[t:]):
        if s == 'x':
            continue
        elif last + C >= i + t:
            continue

        ret.append(i + t)
        last = i + t
    return ret


def GetReverse():
    ret = []
    last = -C * 2 - 1
    for i, s in enumerate(S[::-1]):
        if s == 'x':
            continue
        elif last + C >= i:
            continue

        ret.append(len(S) - 1 - i)
        last = i
    return reversed(ret)


def GetDepend(base_ans):
    ruiseki = []
    a = 0
    for s in S:
        if s == 'o':
            a += 1
            ruiseki.append(a)
        else:
            ruiseki.append(a)

    ret = {a: False for a in base_ans}
    for a in ret:
        if ruiseki[a] == ruiseki[min(N - 1, a + C)]:
            ret[a] = True
    return ret


def solve():
    base_ans = GetBase()
    if len(base_ans) > K:
        return []

    reverse_ans = GetReverse()

    return sorted(list(set(base_ans) & set(reverse_ans)))


N, K, C = inpl()
S = list(input().strip())

ans = solve()

for a in ans:
    print(a + 1)
