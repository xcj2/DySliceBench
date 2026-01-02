#coding:utf-8
import sys,os
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
from collections import Counter, deque
from random import random
class Node:
        def __init__(self,value:int=-1):
            self.left = None
            self.right = None
            self.value = value
            self.priority = int(random()*10**7)
            self.count_partial = 1
            self.calc_partial = value
class Treap:
    
    def __init__(self,func=None):
        self.root = None
        self.func = lambda x,y,z:x+y+z if func is None else func

    def size(self, node:Node):
        return 0 if node is None else node.count_partial
    
    def calc_result(self, node):
        return 0 if node is None else node.calc_partial
    
    def node_key(self, node:None):
        return -1 if node is None else node.key

    def update(self, node):
        # if node.left is None:
        #     left_count = 0
        #     left_sum = 0
        # else:
        #     left_count = node.left.count_partial
        #     left_sum = node.left.sum_partial
        # if node.right is None:
        #     right_count = 0
        #     right_sum = 0
        # else:
        #     right_count = node.right.count_partial
        #     right_sum = node.right.sum_partial  

        node.count_partial = self.size(node.left) + self.size(node.right) + 1
        node.calc_partial = self.func(self.calc_result(node.left),node.value,self.calc_result(node.right))
        return node

    def merge(self, left :Node, right:Node):
        if left is None or right is None:
            return left if right is None else right

        if left.priority > right.priority:
            left.right = self.merge(left.right,right)
            # return self.update(left)
            return self.update(left)
        else:
            right.left = self.merge(left,right.left)
            # return self.update(right)
            return self.update(right)




    #指定された場所のノードは右の木に含まれる

    # def split(self, node:Node, key:int, level=0):
    #     if node is None:
    #         return (None,None)

    #     if key <= self.node_size(node.left):
    #         left,right = self.split(node.left, key,level+1)
    #         node.left = right
    #         return left, self.update(node)
    #     else:
    #         left,right = self.split(node.right, key - self.node_size(node.left) - 1,level+1)
    #         node.right = left
    #         return self.update(node),right 
    def split(self, node:None, value):
        if node is None:
            return None,None
        if value <= node.value:
            left,right = self.split(node.left, value)
            node.left = right
            return left, self.update(node)
        else:
            left,right = self.split(node.right, value)
            node.right = left
            return self.update(node),right

    
    def insert(self, pos:int,value:int =-1):
        value = value if value > 0 else pos
        left, right = self.split(self.root, pos)
        new_node = Node(value)
        self.root = self.merge(self.merge(left,new_node),right)
    
    def erase(self, pos:int):
        middle,right = self.split(self.root, pos+1)
        left,middle = self.split(middle, pos)
        self.root = self.merge(left,right)

        

    def printTree(self, node=None, level=0):
        node = self.root if node is None else node
        if node is None:
            print('level=',level,'root is None')
            return
        else:
            print('level=',level,'v=',node.value,'c=',node.count_partial, 'p=',node.priority)
        if node.left is not None:
            self.printTree(node.left,level+1)
        
        if node.right is not None:
            self.printTree(node.right,level+1)
        
    

    def search(self, pos):
        #return self.search_recursively(pos,self.root)
        v = self.root
        while v:
            left_count = self.node_size(v.left)
            if pos < left_count:
                v = v.left
            elif pos == left_count:
                return v.value
            else:
                v = v.right
                pos -= left_count + 1
        return -1

    def search2(self, value):
        v = self.root
        upper = 10**18
        while v:

            if value == v.value:
                return value

            elif value < v.value:
                upper = v.value
                v = v.left
            else:
                v = v.right
        return upper

    def search_recursively(self, pos, node):
        if node is None:
            return -1
        num_left = 0 if node.left is None else node.left.count_partial
        if num_left + 1 == pos:
            return node.value
        if pos <= num_left:
            return self.search_recursively(pos, node.left)
        else:
            return self.search_recursively(pos - num_left - 1, node.right)
        


    
                










def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    N = II()
    S = list(map(lambda c: ord(c) - ord('a'), list(input())))



    trees = []
    for i in range(26):
        trees.append(Treap())
    

    for i,c in enumerate(S):
        trees[c].insert(i)
    
    Q = int(input())
    out = []
    for _ in range(Q):
        q1,q2,q3 = input().split()
        if int(q1) == 1:
            iq = int(q2)-1
            before = S[iq]
            after = ord(q3)-ord('a')
            S[iq] = after
            trees[before].erase(iq)
            trees[after].insert(iq)

        else:
            l,r = int(q2)-1,int(q3)-1
            count = 0
            for i in range(26):
                if trees[i].search2(l) <= r:
                    count += 1
            out.append(count)
    print('\n'.join(map(str,out)))


if __name__ == '__main__':
    main()