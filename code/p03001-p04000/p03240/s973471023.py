def checkheight(H, data, coordinate):
    cx, cy = coordinate

    for px, py, ph in data:
        if not ph == max(H - abs(px - cx) -  abs(py - cy), 0):
            return None

    return (cx, cy, H)

def makeheight(data, cx, cy):
    px, py, ph = list(filter(lambda dataset: dataset[2] > 0, data))[0]
    return ph + abs(px - cx) + abs(py - cy)


def main():
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]


    for cx in range(101):
        for cy in range(101):
            tmpch = makeheight(data.copy(), cx, cy)

            res = checkheight(tmpch, data, (cx, cy))

            if res:
                print(*res)
                return



if __name__ == '__main__':
    main()
