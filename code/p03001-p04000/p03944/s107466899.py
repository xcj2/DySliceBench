def init_rectangle(w, h):
    rectangle = []
    for x in range(w):
        x_list = []
        for y in range(h):
            x_list.append(True)
        rectangle.append(x_list)
    return rectangle

def area(rectangle):
    count = 0
    for i in rectangle:
        for j in i:
            if j:
                count += 1
    return count

def paint_point(rectangle, w, h, x1, x2, y1, y2):
    for x in range(x1, x2):
        for y in range(h):
            rectangle[x][y] = False
    for x in range(w):
        for y in range(y1, y2):
            rectangle[x][y] = False
        
def paint(rectangle, w, h, points):
    for x, y, a in points:
        x1 = x2 = y1 = y2 = 0
        if a == 1:
            x2 = x
        elif a == 2:
            x1 = x
            x2 = w
        elif a == 3:
            y2 = y
        else:
            y1 = y
            y2 = h
        paint_point(rectangle, w, h, x1, x2, y1, y2)


if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    points = [list(map(int, input().split())) for _ in range(n)]
    rectangle = init_rectangle(w, h)
    paint(rectangle, w, h, points)
    print(area(rectangle))