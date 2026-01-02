from collections import deque

def isOneColor(w):
    sw = sorted(w)
    if sw[0] == sw[-1]:
        return True
    else:
        return False

def nextColor(c1, c2):
    cs = ['r', 'g', 'b']
    cs.remove(c1)
    cs.remove(c2)
    return cs[0]

def bfs(iw):
    q = deque()
    s = set()

    s.add(str(iw))
    q.append([iw, 0])
    while q:
        w, t = q.popleft()
        if isOneColor(w):
            return t
        else:
            for i in range(len(w)-1):
                if w[i] != w[i+1]:
                    nw = w.copy()
                    nc = nextColor(nw[i], nw[i+1])
                    nw[i], nw[i+1] = nc, nc
                    if str(nw) not in s:
                        s.add(str(nw))
                        q.append([nw, t+1])

    return -1

if __name__ == '__main__':
    while True:
        w = list(input())
        if w == ['0']:
            break

        t = bfs(w)
        if t == -1:
            print('NA')
        else:
            print(t)