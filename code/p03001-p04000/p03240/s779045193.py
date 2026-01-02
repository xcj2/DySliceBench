class Plot:

    def __init__(self, inp):
        self.x, self.y, self.h = inp


def plot_check(xyh, cx, cy, H):
    for i in xyh:
        if max(H - abs(i.x - cx) - abs(i.y - cy),0) != i.h:
            return False
    return True


def main():
    xyh = []
    kensa = 0
    N = int(input())
    for i in range(N):
        xyh.append(Plot(map(int, input().split())))
    for i in range(len(xyh)):
        if xyh[i].h > 0:
            kensa = i
            break
    for cxi in range(101):
        for cyi in range(101):
            H = abs(xyh[kensa].x - cxi) + abs(xyh[kensa].y - cyi) + xyh[kensa].h
            if plot_check(xyh, cxi, cyi, H):
                print(cxi, cyi, H)
                return


main()