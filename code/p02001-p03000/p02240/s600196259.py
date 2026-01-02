#coding:utf-8

class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
    def find(self,x):
        if self.parent[x] == x: # if x is x`s root
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    def is_same_tree(self,x,y):
        return self.find(x) == self.find(y) 
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        
def main():
    n=list(map(int,input().split()))
    union=UnionFind(n[0])
    friends=[]
    question=[]
    for i in range(n[1]):
        a=tuple(map(int,input().split()))
        friends.append(a)
    for i in friends:
        union.union(i[0],i[1])
    m=int(input())
    for i in range(m):
        b=tuple(map(int,input().split()))
        question.append(b)
    for i in question:
        if union.find(i[0]) == union.find(i[1]):
            print("yes")
        else:
            print("no")
if __name__ == "__main__":
    main()
