import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    h,w = LI()
    board = []
    for _ in range(h):
        line = list(S())
        board.append(line)
    
    wpro = []
    wline = ["." for _ in range(w)]

    for line in board:
        if line != wline:
            wpro.append(line)
    
    hpro = list(zip(*wpro))
    hline = tuple(["." for _ in range(len(hpro[0]))])
    # print(hline)
    ans = []
    # print(hpro)
    for line in hpro:
        if line!= hline:
            ans.append(line)
    
    ans = list(zip(*ans))
    for line in ans:
        print("".join(line))
main()