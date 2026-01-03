import sys
input=sys.stdin.readline
class UnionFindNode(object):
    """
    Union-Find構造
    ノードのグループ併合や、所属グループ判定を高速に処理する
    """

    def __init__(self, group_id, parent=None, value=None):
        self.group_id_ = group_id
        self.parent_ = parent
        self.value = value
        self.size_ = 1

    def __str__(self):
        template = "UnionFindNode(group_id: {}, \n\tparent: {}, value: {}, size: {})"
        return template.format(self.group_id_, self.parent_, self.value, self.size_)

    def is_root(self):
        return not self.parent_

    def root(self):
        parent = self
        while not parent.is_root():
            parent = parent.parent_
            self.parent_ = parent
        return parent

    def find(self):
        parent = self.root()
        return parent.group_id_

    def size(self):
        parent = self.root()
        return parent.size_

    def unite(self, unite_node):
        parent = self.root()
        unite_parent = unite_node.root()

        if parent.group_id_ != unite_parent.group_id_:
            if parent.size() > unite_parent.size():
                unite_parent.parent_ = parent
                parent.size_ = parent.size_ + unite_parent.size_
            else:
                parent.parent_ = unite_parent
                unite_parent.size_ = parent.size_ + unite_parent.size_
    def is_group(self,other):#selfとotherが同じグループに属するか
        return self.root()==other.root()

N=int(input())
X=[]
Y=[]
for i in range(N):
  x,y=map(int,input().split())
  X.append([x,i])
  Y.append([y,i])
X.sort()
Y.sort()
G=[]
for i in range(N-1):
  G.append([X[i+1][0]-X[i][0],X[i][1],X[i+1][1]])
  G.append([Y[i+1][0]-Y[i][0],Y[i][1],Y[i+1][1]])
G.sort()
U=[UnionFindNode(i) for i in range(N)]
ans=0
for i in range(len(G)):
    c,a,b=G[i]
    if U[a].is_group(U[b]):
        continue
    U[a].unite(U[b])
    ans+=c
    if U[0].size()==N:
        print(ans)
        quit()
