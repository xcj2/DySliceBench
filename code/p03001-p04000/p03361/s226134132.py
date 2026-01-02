H, W = map(int, input().split())
s = [[i for i in input()] for _ in range(H)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def check(y, x):
    if s[y][x] == "#":
        for i, j in dir:
            try:
                if s[y+i][x+j] == "#":
                    return True
            except:
                pass
        else:
            return False
    return True
def solve():
    for y in range(H):
        for x in range(W):
            if not check(y, x):
                return False
    return True

def main():
    if solve():
        print("Yes")
    else:
        print("No")

main()
