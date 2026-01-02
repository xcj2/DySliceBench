


class Rectangle:
    def __init__(self, height, position):
        self.height = height
        self.position = position

def getLargestRectangleRow(size, bufTmp):
    S = []
    maxv = 0
    #bufTmp[0] * size
    bufTmp.append(0)
    for i in range(size + 1):
        rect = Rectangle(bufTmp[i], i)
        
        if len(S) == 0:
            S.append(rect)
        else:
            if S[-1].height < rect.height:
                S.append(rect)
            elif S[-1].height > rect.height:
                target = i
                while len(S) >= 1 and S[-1].height >= rect.height:
                    pre = S.pop()
                    area = pre.height * (i-pre.position)
                    maxv = max(maxv, area)
                    target = pre.position
                rect.position = target
                S.append(rect)
    return maxv


def getLargestRectangle():
    for j in range(W):
        for i in range(H):
            if buf[i][j]:
                T[i][j] = 0
            else:
                if i > 0:
                    T[i][j] = T[i-1][j] + 1
                else:
                    T[i][j] = 1
    maxv = 0
    for i in range(H):
        maxv = max(maxv, getLargestRectangleRow(W, T[i]))

    return maxv


nums=list(map(int,input().split()))
H = nums[0]
W = nums[1]
buf = [[0 for i in range(W)] for j in range(H)]
T = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
    nums=list(map(int,input().split()))
    for j in range(W):
        buf[i][j] = nums[j]

print(getLargestRectangle())




















