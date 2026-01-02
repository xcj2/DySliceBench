# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_B&lang=jp
# Binary Search Tree II: python3
# 2018.11.27 yonezawa

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
            else:
                self.setChild(n,cn.c_right)
        else:
            if (cn.c_left == None):
                cn.c_left = node(n) 
                cn.c_left.parent =  cn 
            else:
                self.setChild(n,cn.c_left)

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
    
    def getRoot(self):
        if (self.parent == None):
            return self
        return self.parent.getRoot()

def main():
    n = int(input())
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
            else:
                root.setChild(d)
        elif (l[0] == "find"):
            d = int(l[1])
            r = root.find(d)
            if (r == True):
                print ("yes")
            else:
                print ("no")

if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()
