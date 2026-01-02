n = int(input())
a_ls = list(map(int, input().split()))
b_ls = list(map(int, input().split()))
c_ls = list(map(int, input().split()))
a_ls.sort()
b_ls.sort()
c_ls.sort()

# 「-より大きい」
def isOK_1(ind, key, ls):
    if ls[ind] > key:
        return True
    else: # if ls[ind] <= key
        return False


def connect_b2c_minind(key, ls):
    ok = len(ls)
    ng = -1
    while ok - ng > 1:
        mid = ng + (ok-ng) // 2
        if isOK_1(mid, key, ls):
            ok = mid
        else:
            ng = mid
    return len(ls) - ok

def isOK_2(ind, key, ls):
    if ls[ind] < key:
        return True
    else: # if ls[ind] >= key
        return False

def connect_a2b_maxind(key, ls):
    ok = -1
    ng = len(ls)
    while ng - ok > 1:
        mid = ok + (ng - ok) // 2
        if isOK_2(mid, key, ls):
            ok = mid
        else:
            ng = mid
    return ok + 1

ans = 0
for i in range(n):
    ans += connect_a2b_maxind(b_ls[i], a_ls) * connect_b2c_minind(b_ls[i], c_ls)
print(ans)