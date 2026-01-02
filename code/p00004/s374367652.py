import sys

def inv(k):
    det = 1 / (k[0]*k[3] - k[1]*k[2])
    ret = [k[3] * det, -k[1] * det, -k[2] * det, k[0] * det]
    return ret

def dot(i, j):
    x = i[0] * j[0] + i[1] * j[1]
    y = i[2] * j[0] + i[3] * j[1]
    return [x,y]

def run():
    data = []
    for _data in sys.stdin:
        data.append(list(map(int, _data.split())))

    for _data in data:
        i = _data[:2] + _data[3:5]
        j = [_data[2],_data[5]]
        x, y = dot(inv(i), j)
        x, y = round(x, 3), round(y, 3)
        print('{0:.3f} {1:.3f}'.format(x,y))

if __name__ == '__main__':
    run()


