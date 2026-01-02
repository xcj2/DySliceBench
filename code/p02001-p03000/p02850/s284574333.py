#AtCorder用　自動木取得コード

#１行目がノードの数、２行目以降が２つの数字でノードを繋ぐ辺を表すとき、使える

#変数
#node_n :ノードの数
#edge   :エッジを、入力の順番でリストとして提供
#【注意】ノードクラスのリストは関数で取り出さないと、連動して変わってしまう


#関数
#・getroot()で根を取り出す
#・getleaf()で葉を取り出す
#・childに子のノードクラスのリストが格納
#・parentに親のノードクラスが格納

import sys
sys.setrecursionlimit(1000000)



#ノードクラス
class Node():
    def __init__(self):
        self.name=-1
        self.parent=-1
        self.child=[]
        self.color=0
        
        
        
        
    #ノードに対する子供の数を取得
    def childnum(self):
        return len(self.child)

    

#木クラス
class Tree():
    
    
    #作成した瞬間、入力の数だけノードを作る。
    def __init__(self):
        self.tree=[]
        self.edge=[]
        self.node_n=int(input())
        for i in range(self.node_n):
            a=Node()
            a.name=i
            self.tree.append(a)
        for i in range(self.node_n-1):
            edge=[int(j) for j in input().split()]
            self.edge.append(edge)
            self.tree[edge[0]-1].child.append(self.tree[edge[1]-1])
            self.tree[edge[1]-1].parent=self.tree[edge[0]-1]
       
     
    #根ノードを取得
    def getroot(self):
        return self.tree[0]
    
    #葉ノードのリストを取得
    def getleaf(self):
        leaf=[]
        for i in self.tree:
            if i.child==[]:
                leaf.append(i)
        return leaf
    
    
    #全ノードリストを取得
    def gettree(self):
        return self.tree[:]

    
    
    
    
    
tree=Tree()

ans=0
node=tree.getroot()


def dps(Node):
    global ans
    colorlist=[]
    p_col=Node.color
    childnum=Node.childnum()
    for i in range(childnum+1):
        colorlist.append(i+1)
    if p_col in colorlist:
        colorlist.remove(p_col)
    else:
        colorlist.pop()
    
    if colorlist!=[]:
        maxcol=colorlist[-1]
        if maxcol>=ans:
            ans=maxcol
        children=Node.child
        for i in range(childnum):
            children[i].color=colorlist[i]
        for child in children:
            dps(child)
    

dps(node)

print(ans)

tre=tree.gettree()
edge=tree.edge
n=tree.node_n

for i in edge:
    print(tre[i[1]-1].color)
