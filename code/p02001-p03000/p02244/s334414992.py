# coding: utf-8
import sys

stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip() # ignore trailing spaces


def permutation(ret: list, leftovers: list) -> list:
    if len(leftovers) == 0:
        yield ret
    
    for left in leftovers:
        leftoverscopy = [i for i in leftovers]
        leftoverscopy.remove(left)
        yield from permutation(ret+[left], leftoverscopy)


def canAssign(xs, ys):
    for i in range(7):
        for j in range(i+1,8):
            if abs(xs[i]-xs[j]) == abs(ys[i]-ys[j]):
                return False
    return True


def displayChessboard(xs, ys):
    board = [['.']*8 for i in range(8)]
    for i in range(8):
        board[ys[i]][xs[i]] = 'Q'
    for i in range(8):
        for j in range(8):
            print(board[i][j], end='')
        print()
    return


def main():
    k = ni()
    queens = [na() for _ in range(k)]
    xqueens = []
    yqueens = []
    xs = [x for x in range(8)]
    ys = [y for y in range(8)]
    for queen in queens:
        xs.remove(queen[1])
        ys.remove(queen[0])
        xqueens.append(queen[1])
        yqueens.append(queen[0])
    
    for yspernm in permutation([],ys):
        if canAssign(xqueens+xs, yqueens+yspernm):
            displayChessboard(xqueens+xs, yqueens+yspernm)
            return
    
    print("Can't make chessboard.")
    return


if __name__ == '__main__':
    main()
