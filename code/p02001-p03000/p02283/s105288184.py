# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_C&lang=jp
# Binary Search Tree I
# 2018.12.01 yonezawa

import sys
input = sys.stdin.readline
import cProfile

class node:
    def __init__(self,nodeid):
        self.parent = None
        self.c_left = None
        self.c_right = None
        self.nodeid = nodeid
    def setChild(self,n,cn=None):
        if (cn == None):
            cn = self
        if ( cn.nodeid < n):
            if (cn.c_right == None):
                cn.c_right = node(n) 
                cn.c_right.parent =  cn 
                return cn.c_right
            else:
                return self.setChild(n,cn.c_right)
        else:
            if (cn.c_left == None):
                cn.c_left = node(n) 
                cn.c_left.parent =  cn
                return cn.c_left 
            else:
                return self.setChild(n,cn.c_left)

    def getPreorder(self,r1=[]):
        r1.append(self.nodeid)
        if (self.c_left != None):
            r1 = self.c_left.getPreorder(r1)
        if (self.c_right != None):
            r1 = self.c_right.getPreorder(r1)
        return r1       
    def getInorder(self,r1=[]):
        if (self.c_left != None):
            r1 = self.c_left.getInorder(r1)
        r1.append(self.nodeid)
        if (self.c_right != None):
            r1 = self.c_right.getInorder(r1)
        return r1       
    def getPostorder(self,r1=[]):
        if (self.c_left != None):
            r1 = self.c_left.getPostorder(r1)
        if (self.c_right != None):
            r1 = self.c_right.getPostorder(r1)
        r1.append(self.nodeid)
        return r1       
    def find(self,n):
        if self.nodeid == n:
            return True
        if self.nodeid > n:
            if (self.c_left == None ):
                return False
            return self.c_left.find(n)
        else:
            if  (self.c_right == None):
                return False
            return self.c_right.find(n)

    def findObject(self,n):
        if self.nodeid == n:
            return self
        if self.nodeid > n:
            if (self.c_left == None ):
                return None
            return self.c_left.findObject(n)
        else:
            if  (self.c_right == None):
                return None
            return self.c_right.findObject(n)

    def deleteNum(self,n):
        i = self.findObject(int(n))
        if i == None:
            return False
        self.deleteObject(i)
        return True

    def deleteObject(self,obj):
        p = obj.parent
        x = obj
        if x.c_left == None and x.c_right == None:
            if p.c_right.nodeid == x.nodeid:
                p.c_right = None
            else:
                p.c_left = None
            x.nodeid = -1
            x.parent = None
            x.c_right = None
            x.c_left = None
            return

        if x.c_left == None and x.c_right != None:
            if p.c_right != None and p.c_right.nodeid == obj.nodeid:
                p.c_right = x.c_right
                x.c_right.parent = p
            else:
                p.c_left = x.c_right
                x.c_right.parent = p
            x.nodeid = -1
            x.parent = None
            x.c_right = None
            x.c_left = None
            return

        if x.c_left != None and x.c_right == None:
            if p.c_right.nodeid == x.nodeid:
                p.c_right = x.c_left
                x.c_left.parent = p
            else:
                p.c_left = x.c_left
                x.c_left.parent = p
            x.nodeid = -1
            x.parent = None
            x.c_right = None
            x.c_left = None
            return

        y = self.findMinObject(x.c_right)
        x.nodeid = y.nodeid
        p = y.parent
        x = y
        if x.c_left == None and x.c_right == None:
            if p.c_right != None and p.c_right.nodeid == x.nodeid:
                p.c_right = None
            else:
                p.c_left = None
            x.nodeid = -1
            x.parent = None
            x.c_right = None
            x.c_left = None
            return

        if x.c_left == None and x.c_right != None:
            if p.c_right.nodeid == obj.nodeid:
                p.c_right = x.c_right
                x.c_right.parent = p
            else:
                p.c_left = x.c_right
                x.c_right.parent = p
            x.nodeid = -1
            x.parent = None
            x.c_right = None
            x.c_left = None
            return

    def findMinObject(self,obj):
        i = obj
        while i != None and i.c_left != None:
            i = i.c_left
        return i

    
    def getRoot(self):
        if (self.parent == None):
            return self
        return self.parent.getRoot()

def printNodeList(nodelist,caption):
    for i in nodelist:
        a = b = c = None
        if (i != None ):
            a = i.nodeid
        if (i.c_left != None):
            b = i.c_left.nodeid
        if (i.c_right != None):
            c = i.c_right.nodeid 
        if ( a != None and (b != None or c != None)):
            print (caption,a,b,c)
            
def main():
    n = int(input())
    nodelist = []
    root = None
    for i in range(n):
        l = list(map(str,input().split()))
        if (l[0] == "print" and root != None):
            print("",*root.getInorder([]))
            print("",*root.getPreorder([]))
        elif (l[0] == "insert"):
            d = int(l[1])
            if ( root == None):
                root = node(d)
                nodelist.append(root)
            else:
                #root.setChild(d)
                nodelist.append(root.setChild(d))
        elif (l[0] == "find"):
            d = int(l[1])
            r = root.find(d)
            if (r == True):
                print ("yes")
            else:
                print ("no")
        elif (l[0] == "delete"):
            #printNodeList(nodelist,"Debug:rm "+str(l[1])+":")
            root.deleteNum(l[1])
            #printNodeList(nodelist,"Debug:post rm "+str(l[1])+":")

        
if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()
