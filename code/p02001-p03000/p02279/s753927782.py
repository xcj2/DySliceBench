class Node:
    def __init__(self,parent = -1,childs = []):
        self.p = parent
        self.c = childs


def main():
    n = int(input())
    t = [Node() for _ in range(n)]
    for i in range(n):
        b = list(map(int,input().split()))
        t[b[0]].c = b[2:]
        for d in b[2:]:t[d].p = b[0]

    def depth(i):
        res = 0
        while t[i].p!=-1:
            i = t[i].p
            res+=1
        return res

    for i in range(n):
        print('node %d: parent = %d, '%(i,t[i].p),end='')
        print('depth = %d, '%depth(i),end='')
        if t[i].p==-1      :print ('root,',t[i].c)
        elif len(t[i].c)!=0:print ('internal node,',t[i].c)
        else               :print ('leaf,',t[i].c)

if __name__ == '__main__':
    main()


