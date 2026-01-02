class Rectangle:
    def __init__(self, height, pos):
        self.height = height
        self.pos = pos


def getLargestRectangleInRow(size, buffer):
    s = []
    maxv = 0
    buffer.append(0)
    for i in range(size + 1):
        rect = Rectangle(buffer[i], i)
        if len(s) == 0:
            s.append(rect)
        else:
            if s[-1].height < rect.height:
                s.append(rect)
            elif s[-1].height > rect.height:
                target = i
                while len(s) != 0 and s[-1].height >= rect.height:
                    pre = s.pop()
                    area = pre.height * (i - pre.pos)
                    maxv = max(maxv, area)
                    target = pre.pos
                rect.pos = target
                s.append(rect)

    return maxv


def getLargestRectangle(H, W, buffer):
    t = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if buffer[i][j] == 1:
                t[i][j] = 0
            else:
                if i > 0:
                    t[i][j] = t[i-1][j] + 1
                else:
                    t[i][j] = 1

    maxv = 0
    for i in range(H):
        maxv = max(maxv, getLargestRectangleInRow(W, t[i]))
    return maxv



if __name__ == '__main__':
    h, w = [int(v) for v in input().split()]
    c = []
    for i in range(h):
        c.append([int(v) for v in input().split()])

    print(getLargestRectangle(h, w, c))
