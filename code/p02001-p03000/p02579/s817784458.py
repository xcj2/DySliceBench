import sys
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
sh, sw = map(lambda x: int(x)-1, input().split())
gh, gw = map(lambda x: int(x)-1, input().split())
state = [list(input().rstrip()) for _ in range(H)]

def nexts1(h, w):
    ret = []
    if h != 0: ret.append((h-1, w))
    if h != H-1: ret.append((h+1, w))
    if w != 0: ret.append((h, w-1))
    if w != W-1: ret.append((h, w+1))
    return ret

def nexts2(h, w):
    ret = []
    for nh in range(h-2, h+3):
        for nw in range(w-2, w+3):
            if 0 <= nh < H and 0 <= nw < W:
                ret.append((nh, nw))
    return ret


def bfs():
    checked = [[-1]*W for _ in range(H)]
    P = {(sh, sw)}
    cnt = 0
    while P:
        q = []
        for h, w in P:
            if checked[h][w] == -1:
                checked[h][w] = 1
                q.append((h, w))
        P = set()
        while q:
            qq = []
            for h, w in q:
                if h == gh and w == gw:
                    return cnt
                for nh, nw in nexts1(h, w):
                    if state[nh][nw] == ord(".") and checked[nh][nw] == -1:
                        checked[nh][nw] = checked[h][w]
                        qq.append((nh, nw))
                for nh, nw in nexts2(h, w):
                    if checked[nh][nw] == -1 and state[nh][nw] == ord(".") and not (nh, nw) in P:
                        P.add((nh, nw))
            q = qq
        cnt += 1
    return -1

def main():
    print(bfs())


if __name__ == "__main__":
    main()