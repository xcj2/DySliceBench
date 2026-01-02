import sys

sys.setrecursionlimit(1000000)


n=int(input())

#ノードクラスの定義
class Node:
    def __init__(self,name):
        self.name=name
        self.near=[]
        self.length=[]
    def coloring(self,color):
        self.color=color


#ノードリストの作成
nodelist=[]
for i in range(n):
    nodelist.append(Node(i))
   
    
#辺の作成
for i in range(n-1):
    u,v,w=[int(i) for i in input().split()]
    w=w%2
    nodelist[u-1].near.append(nodelist[v-1])
    nodelist[u-1].length.append(w)
    nodelist[v-1].near.append(nodelist[u-1])
    nodelist[v-1].length.append(w)
    
#行ったかカラーでチェックリスト
color=[None for i in range(n)]
color[0]=0



def paint(node):
    nodecolor=node.color
    for j in range(len(node.near)):
        nearnode=node.near[j]
        if color[nearnode.name]!=None:
            continue
        if node.length[j]==0:
            nearnode.coloring(nodecolor)
        else:
            nearnode.coloring((nodecolor+1)%2)
        color[nearnode.name]=0
        paint(nearnode)

nodelist[0].coloring(0)
paint(nodelist[0])


for i in nodelist:
    print(i.color)
            
        
    