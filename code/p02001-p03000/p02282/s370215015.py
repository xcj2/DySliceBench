from collections import namedtuple
Node = namedtuple('Node', ['parent', 'children'])
   
class my_binary_tree:
    def __init__(self, preorderList, inorderList):
        self.T = {}
        self.reconstruction(preorderList,inorderList)
   
    def reconstruction(self, preorderList, inorderList, parent=-1):
        i = preorderList[0]
        p = parent
        j = inorderList.index(i) 
        llen = len(inorderList[:j])
        rlen = len(inorderList[j+1:])
        if llen > 0: c0 = self.reconstruction(preorderList[1:llen+1],inorderList[:llen],i)
        else       : c0 = -1
        if rlen > 0: c1 = self.reconstruction(preorderList[llen+1:],inorderList[llen+1:],i)
        else       : c1 = -1
        self.T[i] = Node(p,[c0,c1])
        return i
   
    def getPostorderList(self, i):
        c0 = self.T[i].children[0]
        c1 = self.T[i].children[1]
        if c0 != -1: yield from self.getPostorderList(c0)
        if c1 != -1: yield from self.getPostorderList(c1)
        yield i
   
    
if __name__=='__main__':
    n = int(input())
    preorderList = list(map(int,input().split()))
    inorderList  = list(map(int,input().split()))
    tree = my_binary_tree(preorderList,inorderList)
        
    print(*tree.getPostorderList(preorderList[0]))