
N,Q = map(int, input().split())

A = [2**31 - 1] * N

q = [tuple(map(int, input().split())) for _ in range(Q)]

seg_num = 2**(N-1).bit_length()
ide_ele = float("inf")
func = min
seg_lst = [ide_ele] * 2 * seg_num

def init(lst):
    for i in range(N):
        # seg_lst1内のindexに変換
        seg_lst[i + seg_num - 1] = lst[i]
    
    # それぞれのノードについて、子の部分を引き上げてくる
    for i in range(seg_num - 2, -1, -1):
        seg_lst[i] = func(seg_lst[2*i + 1], seg_lst[2*i + 2])

def update(i, x):
    # seg_lst1内のindexに変換
    i += seg_num - 1
    seg_lst[i] = x
    while i:
        # 親に移って子の部分をくみ上げる
        i = (i - 1) // 2
        seg_lst[i] = func(seg_lst[2*i + 1], seg_lst[2*i + 2])

def query(l,r):
    if r <= l:
        return ide_ele

    l += seg_num - 1
    r += seg_num - 2

    ret = ide_ele

    while r - l > 1:

        if l & 1 == 0:
            ret = func(ret, seg_lst[l])
        if r & 1 == 1:
            ret = func(ret, seg_lst[r])
            r -= 1
        l  = l // 2
        r = (r - 1) // 2

    if l == r:
        ret = func(ret, seg_lst[l])
    else:
        ret = func(ret, seg_lst[l])
        ret = func(ret, seg_lst[r])
    return ret


init(A)

for c,x,y in q:
    if c == 0:
        update(x, y)
    else:
        print(query(x, y+1))
