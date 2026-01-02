import sys
from collections import deque
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]


def main():
    move = [[i, j] for i in range(-1,2) for j in range(-1,2) if not(i==j and i == 0)]
    try:
        while True:
            w, h = MI()
            if w == h and h == 0:
                sys.exit()
            d = Init(h, w, True)
            mylist = [LI() for i in range(h)]
            result = 0
            for i in range(h):
                for j in range(w):
                    if d[i][j] and mylist[i][j] == 1:
                        result+=1
                        dq = deque()
                        dq.append([i, j])
                        while dq:
                            x, y = dq.pop()
                            for x2, y2 in move:
                                x2 += x
                                y2 += y
                                if x2 >= 0 and x2 < h and y2 >= 0 and y2 < w:
                                    if mylist[x2][y2] == 1 and d[x2][y2]:
                                        dq.append([x2,y2])
                                        d[x2][y2] = False
                                    elif d[x2][y2]:
                                        d[x2][y2] = False
            print(result)
    except:
        sys.exit()
    
    
    
if __name__ == "__main__":
    main()

