import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**5)

def main():
    N,M = map(int,input().split())
    use = [False for _ in range(N)]
    formula = 0
    
    I = [i for i in range(N)]
    rank = [1 for _ in range(N)]
    def root(x):
        if x == I[x]:
            return x
        I[x] = root(I[x])
        return I[x]
    
    def unite(x,y):
        px,py = root(x),root(y)
        if x < y:
            I[py] = px
        else:
            I[px] = py

    for i in range(M):
        x,y,z = map(int,input().split())
        x -= 1
        y -= 1
        px,py = root(x),root(y)
        if px == py:
            continue
        else:
            unite(x,y)
            formula += 1

    print(N-formula)

if __name__ == "__main__":
    main()