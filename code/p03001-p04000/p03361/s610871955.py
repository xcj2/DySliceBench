def search(X, Y, MAP, H, W):
    if X < 0 or X >= H or Y < 0 or Y >= W:
        return False
    elif MAP[X][Y] == '.':
        return False
    else: 
        return True

def each(X, Y, MAP, H, W):
    right = search(X, Y+1, MAP, H, W)
    down = search(X+1, Y, MAP, H, W)
    left = search(X, Y-1, MAP, H, W)
    up = search(X-1, Y, MAP, H, W)
    return (right or down or left or up)

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                if not each(i, j, s, h, w):
                    print("No")
                    exit()
    print("Yes")

main()