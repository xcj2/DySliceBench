import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    H, W, M = MI()
    hh = [0]*(H+1)
    ww = [0]*(W+1)
    bomb = set()
    for _ in range(M):
        h, w = MI()
        hh[h] += 1
        ww[w] += 1
        bomb.add((h, w))
    h_max = max(hh)
    w_max = max(ww)
    ans = h_max+w_max
    h_index = [i for i, v in enumerate(hh) if v == h_max]
    w_index = [i for i, v in enumerate(ww) if v == w_max]
    flag = True
    for i in h_index:
        for j in w_index:
            if (i, j) not in bomb:
                flag = False
                break
        if not flag:
            break
    if flag:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()