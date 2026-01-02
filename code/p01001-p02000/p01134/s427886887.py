def _f(px, py, qx, qy, rx, ry):
    return (qx - px) * (ry - py) - (qy - py) * (rx - px)

def intersect(px, py, qx, qy, rx, ry, sx, sy):
    f1 = _f(px, py, qx, qy, rx, ry)
    f2 = _f(px, py, qx, qy, sx, sy)
    f3 = _f(rx, ry, sx, sy, px, py)
    f4 = _f(rx, ry, sx, sy, qx, qy)
    
    return f1 * f2 < 0 and f3 * f4 < 0

def intersection(px, py, qx, qy, rx, ry, sx, sy):
    det = (px - qx) * (sy - ry) - (sx - rx) * (py - qy)
    t = ((sy - ry) * (sx - qx) + (rx - sx) * (sy - qy)) / det
    
    x = t * px + (1 - t) * qx
    y = t * py + (1 - t) * qy
    
    return (x, y)

def solve():
    from sys import stdin
    f_i = stdin
    
    while True:
        n = int(f_i.readline())
        if n == 0:
            break
        
        area = 1
        segments = set()
        
        for i in range(n):
            px, py, qx, qy = map(int, f_i.readline().split())
            points = set()
            cnt = 1
            
            for rx, ry, sx, sy in segments:
                if intersect(px, py, qx, qy, rx, ry, sx, sy):
                    ip = intersection(px, py, qx, qy, rx, ry, sx, sy)
                    if ip not in points:
                        cnt += 1
                        points.add(ip)
                        
            segments.add((px, py, qx, qy))
            
            area += cnt
        
        print(area)

solve()
