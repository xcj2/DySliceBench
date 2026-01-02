# 区間和の計算と要素の更新が高速で必要
# l,rごとにやっていると日が暮れる→要素ごとに何回カウントされるかを考える
# 自分より左に大なもの1つ　かつ　右は0個
# 自分より右に大なもの1つ　かつ　左は0個
n = int(input())
P = list(map(int, input().split()))

# segment tree
# 1-index
# A[0]はSEG[num]に。A[n]はSEG[num+n]に
# SEG[i]の下はSEG[2i], SEG[2i+1]
# SEG[i]の上はSEG[i//2]
num = 2 ** (n.bit_length())
ele = 0
SEG = [ele] * (2 * num)


def func(a, b):
    return a + b


def update(idx, x):
    idx += num
    SEG[idx] += x
    idx //= 2
    while idx > 0:
        SEG[idx] = func(SEG[2 * idx], SEG[2 * idx + 1])
        idx //= 2


# [a,b)で定義
def query(a, b):
    a += num
    b += num - 1
    res = ele
    while b - a > 0:
        if a & 1 == 1:
            res = func(res, SEG[a])
            a += 1
        if b & 1 == 0:
            res = func(res, SEG[b])
            b -= 1
        a //= 2
        b //= 2
    if b == a:
        res = func(res, SEG[b])
    return res


def nibutan1(a):
    ok1 = a
    ng = n
    while ng - ok1 > 1:
        mid = (ng + ok1) // 2
        if query(a, mid + 1) == 0:
            ok1 = mid
        else:
            ng = mid
    if ok1 == n - 1:
        return n - 1, n - 1
    ok2 = 0
    ok2 += ok1
    ng = n
    while ng - ok2 > 1:
        mid = (ng + ok2) // 2
        if query(a, mid + 1) == 1:
            ok2 = mid
        else:
            ng = mid
    return ok1, ok2


def nibutan2(a):
    ok1 = a
    ng = -1
    while ok1 - ng > 1:
        mid = (ng + ok1) // 2
        if query(mid, a + 1) == 0:
            ok1 = mid
        else:
            ng = mid
    if ok1 == 0:
        return 0, 0
    ok2 = 0
    ok2 += ok1
    ng = -1
    while ok2 - ng > 1:
        mid = (ng + ok2) // 2
        if query(mid, a + 1) == 1:
            ok2 = mid
        else:
            ng = mid

    return ok1, ok2


A = [None] * n
for idx, v in enumerate(P):
    A[idx] = (v, idx)
A.sort(reverse=True)
ans = 0
for v, idx in A:
    migi1, migi2 = nibutan1(idx)
    hidari1, hidari2 = nibutan2(idx)
    # print("num", v, "idx", idx)
    # print(hidari1, hidari2, migi1, migi2)
    if migi1 == n - 1 and hidari1 == 0:
        pass
    elif migi1 == n - 1:
        ans += v * (migi1 - idx + 1) * (hidari1 - hidari2)
    elif hidari1 == 0:
        ans += v * (idx - hidari1 + 1) * (migi2 - migi1)
    else:
        ans += v * (migi1 - idx + 1) * (hidari1 - hidari2)
        ans += v * (idx - hidari1 + 1) * (migi2 - migi1)
    # print("ans", ans)
    update(idx, 1)
print(ans)
