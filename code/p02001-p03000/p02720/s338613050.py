import sys
input = sys.stdin.readline


def inpl():
    return list(map(int, input().split()))


def Get(i):
    ans[i] = []
    for v in ans[i - 1]:
        if v[-1] == '0':
            ans[i].append(v + '0')
            ans[i].append(v + '1')
        elif v[-1] == '9':
            ans[i].append(v + '8')
            ans[i].append(v + '9')
        else:
            t = v[-1]
            ans[i].append(v + str(int(t) - 1))
            ans[i].append(v + str(int(t)))
            ans[i].append(v + str(int(t) + 1))


def GetValueIndex(K):
    i = 1
    while True:
        if len(ans[i]) < K:
            K -= len(ans[i])
            i += 1
        else:
            ans[i].sort()
            return ans[i][K - 1]


K = int(input())

ans = {1: [str(i) for i in range(1, 10)]}
i = 2
while sum(len(v) for v in ans.values()) < K:
    Get(i)
    i += 1

print(GetValueIndex(K))
