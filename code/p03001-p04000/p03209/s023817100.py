n, x = map(int, input().split())
def patty(L):
# レベルLバーガーにパティがいくらあるか
    p = 1
    for i in range(L):
        p = 2 * p + 1
    return (p)
def vol(L):
# レベルLバーガーが何層か
    m = 1
    for i in range(L):
        m  = m * 2 + 3
    return (m)
def eated(L, X):
# レベルLバーガーを下からX層に何枚パティがあるか
    if L == 0:
        return 1
    m = vol(L)
    if X == 1 or X == 0:
        #print("下から１枚")
        return 0
    elif X == (m + 1) / 2:
        #print("ちょうど真ん中")
        #print(str(L-1) + "バーガーのパティ＋１枚")
        return patty(L-1) + 1
    elif X < (m + 1) / 2:
        #print("下半分")
        #print(str(L-1) + "バーガーを考える")
        return eated(L-1, X-1)
    else:
        #print("上半分")
        #print(str(L) + "バーガーのパティを上から" + str(X) + "枚食べたと考える")
        return patty(L) - eated(L, m - X)
print(eated(n, x))