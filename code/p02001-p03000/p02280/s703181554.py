class Node:
    def __init__(self):
        self.c = []
        self.p = -1
        self.sib = -1

def main():
    n = int(input())
    t = [Node() for _ in range(n)]
    for _ in range(n):
        a,b,c = map(int,input().split())
        t[a].c = [b,c]
        if b!=-1:
            t[b].p = a
            t[b].sib = c
        if c!=-1:
            t[c].p = a
            t[c].sib = b

    def depth(i):
        res = 0
        while t[i].p!=-1:
            i = t[i].p
            res+=1
        return res

    def height(i):
        res = 0
        if t[i].c[0]!=-1:res = max(res,height(t[i].c[0])+1)
        if t[i].c[1]!=-1:res = max(res,height(t[i].c[1])+1)
        return res

    for i in range(n):
        print ('node %d: parent = %d, sibling = %d, degree = %d, '%(i, t[i].p, t[i].sib, 2-t[i].c.count(-1)),end='')
        print ('depth = %d, height = %d, '%(depth(i),height(i)),end='')
        if t[i].p==-1           :print ('root')
        elif t[i].c.count(-1)==2:print ('leaf')
        else                    :print ('internal node')


if __name__ == '__main__':
    main()


