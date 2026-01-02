h, w = map(int, input().split())
s = [[c for c in input()] for _ in range(h)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def count_bom(i, j):
    count = 0

    for k in range(8):
        cx = j + dx[k]
        cy = i + dy[k]

        if (cx < 0 or cx >= w):
            continue
        if (cy < 0 or cy >= h):
            continue
        count += check(s[cy][cx])

    return count

def check(symbol):
    if (symbol == "#"):
        return 1
    else:
        return 0

def main():
    ans = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if (s[i][j] == "."):
                ans[i][j] = count_bom(i, j)
            else:
                ans[i][j] = "#"

    for a in ans:
        for b in a:
            print(b, end="")
        print()

if __name__ == '__main__':
    main()