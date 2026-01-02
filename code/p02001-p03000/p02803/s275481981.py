from collections import deque
import numpy as np
def main():
    hw = list(map(int, input().split()))
    s = np.zeros((hw[0],hw[1]), dtype=int)
    validpoints = []
    for i in range(hw[0]):
        tmp = input()
        tm = [None]*hw[1]
        for j in range(hw[1]):
            if tmp[j] == '.':
                tm[j] = 0
                validpoints.append((i,j))
            elif tmp[j] == '#':
                tm[j] = 1
        s[i] = np.array(tm)

    ma = 0

    for i in validpoints:
        cost = breadth(s,i)
        if cost > ma:
            ma = cost
    print(ma)

def breadth(ss, start):
    q = deque()
    visited = np.array(ss)
    visited[start] = 1
    q.append({start})
    c = 0

    while not len(q) == 0:
        c += 1
        v = q.pop()
        tmpl = []
        for i in v:
            visited[i] = 1
            child = get_child_quad(ss, visited, i)
            tmpl.extend(child)
        tmps = set(tmpl)
        if len(tmps) > 0:
            for i in tmps:
                visited[i] = 1
            q.append(set(tmpl))

    return c-1

def get_child_quad(ss, visited, p):
    down = (p[0]+1,p[1])
    up = (p[0]-1,p[1])
    right = (p[0],p[1]+1)
    left = (p[0],p[1]-1)
    child = [down,up,right,left]
    return list(filter(lambda pp: 0 <= pp[0] < len(ss) and 0 <= pp[1] < len(ss[0]) and visited[pp[0],pp[1]] == 0, child))

if __name__ == '__main__':
    main()