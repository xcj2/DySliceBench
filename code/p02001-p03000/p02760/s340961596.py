import sys
input = sys.stdin.readline

def readlines(n):
    for i in range(n):
        for j, x in enumerate(input().split()):
            yield int(x), (i, j)

def bingo(card):
    if any(all(row) for row in card):
        return True
    
    if any(all(row[i] for row in card) for i in range(3)):
        return True
    
    if all(card[i][i] for i in range(3)):
        return True

    if all(card[2-i][i] for i in range(3)):
        return True

def main():
    A = dict(readlines(3))
    card = [[False]*3 for _ in range(3)]
    n = int(input())
    for _ in range(n):
        b = int(input())
        if b in A:
            y, x = A[b]
            card[y][x] = True
        if bingo(card):
            print("Yes")
            return
    
    print("No")


main()
