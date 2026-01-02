# coding: UTF-8
#@document_it
from collections import deque
def document_it(func):
    def new_function(*args,**kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Kewword arguments:', kwargs)
        result = func(*args,**kwargs)
        print('Result:', result)
        return result
    return new_function
###########################

#@document_it
#O(1)のはず
def nb(i,j,H,W):
    ans = []
    a = i+1
    b = i-1
    c = j+1
    d = j-1
    if a >= 0 and a <= H-1:
        ans.append((a,j))
    if b >= 0 and b <= H-1:
        ans.append((b,j))
    if c >= 0 and c <= W-1:
        ans.append((i,c))
    if d >= 0 and d <= W-1:
        ans.append((i,d))
    return ans
        

def e():
    #入力データ整理
    dist={}
    white = {}
    wtotal = 0
    H,W = map(int,input().split())
    for i in range(H):
        row = input()
        for j in range(W):
            dist[(i,j)] = -1
            if row[j] == '.':
                white[(i,j)] = True
                wtotal += 1
            else:
                white[(i,j)] = False
    #リンク作成
    #tuple -> [tuple]
    #リンクの数は最大でも頂点の4倍なのでO(HW)
    link = {}
    for i in range(H):
        for j in range(W):
            link[(i,j)] = []
            if not white[(i,j)]:
                continue
            else:
                nlist = nb(i,j,H,W)
                for p in nlist:
                    if white[p]:
                        link[(i,j)].append(p)
    
    q = deque()
    dist[(0,0)] = 1
    q.append((0,0))
    while q:
        v = q.popleft()
        for w in link[v]:
            if dist[w] == -1:
                dist[w] = dist[v] + 1
                q.append(w)
                #print(w,dist[w])
    if dist[(H-1,W-1)] != -1:
        ans = wtotal - dist[(H-1,W-1)]
    else:
        ans = -1
    #print(wtotal)
    #print(dist[(H-1,W-1)])
                    
    print(ans)

###########################
if __name__ == '__main__':
    e()