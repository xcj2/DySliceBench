H, W = [int(_) for _ in input().split()]
a = [input() for _ in range(H)]

def turnover(hw):
    l1 = len(hw)
    l2 = len(hw[0])
    wh = ['' for _ in range(l2)]
    for i in range(0, l1):
        for j in range(0, l2):
            wh[j] += hw[i][j]
    return wh

def adjustHeight(hw):
    l2 = len(hw[0])
    for i in range(0, len(hw)):
        if hw[i] == '.' * l2:
            del hw[i]
            return adjustHeight(hw)
    return hw

def adjustWidth(hw):
    wh = turnover(hw)
    return turnover(adjustHeight(wh))

[print(_) for _ in adjustWidth(adjustHeight(a))]