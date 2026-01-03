from bisect import*
class BTreeNode:
    def __init__(self):self.key,self.child=[],[]
class BTree:
    def __init__(self):self.root=BTreeNode()
    def search_higher(self,key):
        ptr=self.root
        ret=None
        while ptr.child:
            i=bisect(ptr.key,key)
            if i!=len(ptr.key):ret=ptr.key[i]
            ptr=ptr.child[i]
        i=bisect(ptr.key,key)
        if i!=len(ptr.key):ret=ptr.key[i]
        return ret
    def search_lower(self,key):
        ptr=self.root
        ret=None
        while ptr.child:
            i=bisect_left(ptr.key,key)
            if i:ret=ptr.key[i-1]
            ptr=ptr.child[i]
        i=bisect_left(ptr.key,key)
        if i:ret=ptr.key[i-1]
        return ret
    def insert(self,key):
        def insert_rec(ptr):
            b_size=256
            if not ptr.child:
                insort(ptr.key,key)
                if len(ptr.key)==b_size*2-1:
                    ret=BTreeNode()
                    ret.key=ptr.key[:b_size]
                    ptr.key=ptr.key[b_size:]
                    return ret
            else:
                i=bisect(ptr.key,key)
                tmp=insert_rec(ptr.child[i])
                if tmp:
                    ptr.key.insert(i,tmp.key.pop())
                    ptr.child.insert(i,tmp)
                    if len(ptr.child)==b_size*2:
                        ret=BTreeNode()
                        ret.child=ptr.child[:b_size]
                        ptr.child=ptr.child[b_size:]
                        ret.key=ptr.key[:b_size]
                        ptr.key=ptr.key[b_size:]
                        return ret
        tmp=insert_rec(self.root)
        if tmp:
            root=BTreeNode()
            root.key=[tmp.key.pop()]
            root.child=[tmp,self.root]
            self.root=root
def main():
    n,*a=map(int,open(0).read().split())
    l=[0]*n
    for i,v in enumerate(a,1):l[v-1]=i
    t=BTree()
    t.insert(0)
    t.insert(n+1)
    c=0
    for i,v in enumerate(l,1):
        c+=(t.search_higher(v)-v)*(v-t.search_lower(v))*i
        t.insert(v)
    print(c)
main()