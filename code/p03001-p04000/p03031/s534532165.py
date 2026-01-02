N, M = map(int, input().split())
kss = []
for i in range(M):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    s = tmp[1:]
    kss.append([k, s])
ps = list(map(int, input().split()))

def check_on(s_all, s, p):
    oncnt = 0
    for i in s:
        if s_all[i]:
            oncnt += 1
    if oncnt % 2 == p:
        return True
    else:
        return False

def check_all_on(s_all, kss, ps):
    for i in range(M):
        s = kss[i][1]
        p = ps[i]
        if not check_on(s_all, s, p):
            return False
    return True


def rec(s_all, kss, ps, cnt):
    if len(s_all) == N+1:
        if check_all_on(s_all, kss, ps):
            cnt[0] += 1
            return
    else:
        s_all.append(0)
        rec(s_all, kss, ps, cnt)
        s_all.pop()

        s_all.append(1)
        rec(s_all, kss, ps, cnt)
        s_all.pop()

s_all = [0]
cnt = [0]
rec(s_all, kss, ps, cnt)
print(cnt[0])
