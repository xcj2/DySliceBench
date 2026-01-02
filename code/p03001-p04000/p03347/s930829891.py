import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def LILI(n): return [LI() for _ in range(n)]
INF = 10 ** 18
MOD = 10 ** 9 + 7

'''MEMO:
うしろから見ていく。
0なら、一つ前が0,1なら次へ。
高さhのとき：
    そのますもふくめて前にh+1ますなければ：-1
    あれば：+h回の操作
        次のますがh-1となっているか？
        なっていれば：さらに次
        なっていなければ：はじめから
'''

def main(): 
    N = II()
    A = []
    for i in range(N):
        A.append((i, II()))
    
    action = 0
    prev_h = 0
    for i, h in reversed(A):
        if h == 0:
            if prev_h <= 1:
                pass
            else:
                print(-1)
                return
        else:
            if i < h:
                print(-1)
                return
            else:
                if prev_h == 0 or prev_h < h+1:
                    action += h
                elif prev_h > h+1:
                    print(-1)
                    return
                else:
                    pass
        prev_h = h
    print(action)



main()