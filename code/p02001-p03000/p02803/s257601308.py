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
    # for i in validpoints:
    #     for j in validpoints:
    #         vis = np.array(s)
    #         cost = breadth(s,i,j,vis)
    #         if cost > ma:
    #             ma = cost
    for i in validpoints:
        cost = breadth(s,i)
        if cost > ma:
            ma = cost
    print(ma)

    # print(breadth(s,(2,0),(0,4)))
    # print(breadth(s,(0,0),(1,0)))

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

# def breadth(ss, start, goal, visited):
#     newvis = np.array(visited)
#     newvis[start] = 1
#     if start == goal:
#         return 0
#     down = (start[0]+1,start[1])
#     up = (start[0]-1,start[1])
#     right = (start[0],start[1]+1)
#     left = (start[0],start[1]-1)
#     child = [down,up,right,left]
#     child = list(filter(lambda i: 0 <= i[0] < len(ss) and 0 <= i[1] < len(ss[0]) and visited[i[0],i[1]] == 0, child))
#     if len(child) > 0:
#         mi = 99999
#         for i in child:
#             co = breadth(ss,i,goal,newvis)
#             if mi > co:
#                 mi = co
#         return 1+mi
#     else:
#         return 1
    

# def breadth(ss, start, goal):
#     q = deque()
#     visited = np.array(ss)
#     visited[start] = 1
#     q.append(start)
#     c = 0
#     while not len(q) == 0:
#         v = q.pop()
#         if v == goal:
#             break
#         down = (v[0]+1,v[1])
#         up = (v[0]-1,v[1])
#         right = (v[0],v[1]+1)
#         left = (v[0],v[1]-1)
#         child = [down,up,right,left]
#         child = list(filter(lambda i: 0 <= i[0] < len(ss) and 0 <= i[1] < len(ss[0]) and visited[i[0],i[1]] == 0, child))

#         if len(child) > 0:
#             for i in child:
#                 visited[i] = 1
#                 q.append(i)
#             c += 1
        
#     return c

if __name__ == '__main__':
    main()