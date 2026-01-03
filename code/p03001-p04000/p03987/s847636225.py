from bisect import*
class BTreeNode:
    def __init__(self):self.key,self.child=[],[]
root=BTreeNode()
def main():
    def search_higher(key):
        ptr=root
        ret=None
        while ptr.child:
            i=bisect(ptr.key,key)
            if i!=len(ptr.key):ret=ptr.key[i]
            ptr=ptr.child[i]
        i=bisect(ptr.key,key)
        if i!=len(ptr.key):ret=ptr.key[i]
        return ret
    def search_lower(key):
        ptr=root
        ret=None
        while ptr.child:
            i=bisect_left(ptr.key,key)
            if i:ret=ptr.key[i-1]
            ptr=ptr.child[i]
        i=bisect_left(ptr.key,key)
        if i:ret=ptr.key[i-1]
        return ret
    def insert_rec(ptr,key):
        b_size=512
        if not ptr.child:
            insort(ptr.key,key)
            if len(ptr.key)==b_size*2-1:
                ret=BTreeNode()
                ret.key=ptr.key[:b_size]
                ptr.key=ptr.key[b_size:]
                return ret
        else:
            i=bisect(ptr.key,key)
            tmp=insert_rec(ptr.child[i],key)
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
    def insert(key):
        global root
        tmp=insert_rec(root,key)
        if tmp:
            p=BTreeNode()
            p.key=[tmp.key.pop()]
            p.child=[tmp,root]
            root=p
    n,*a=map(int,open(0).read().split())
    l=[0]*n
    for i,v in enumerate(a,1):l[v-1]=i
    insert(0)
    insert(n+1)
    c=0
    for i,v in enumerate(l,1):
        c+=(search_higher(v)-v)*(v-search_lower(v))*i
        insert(v)
    print(c)
main()