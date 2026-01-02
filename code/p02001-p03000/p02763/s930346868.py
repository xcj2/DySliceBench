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
            self.priority = random()
            # self.count_partial = 1
            # self.sum_partial = value
class Treap:
    
    #Node [left, right, key, value, priority]
    def __init__(self):
        self.root = None

    # def update(self, node):
    #     if node.left is None:
    #         left_count = 0
    #         left_sum = 0
    #     else:
    #         left_count = node.left.count_partial
    #         left_sum = node.left.sum_partial
    #     if node.right is None:
    #         right_count = 0
    #         right_sum = 0
    #     else:
    #         right_count = node.right.count_partial
    #         right_sum = node.right.sum_partial

    #     node.count_partial = left_count + right_count + 1
    #     node.sum_partial = left_sum + right_sum + node.value
    #     return node

    def merge(self, left_tree, right_tree):
        if left_tree is None or right_tree is None:
            return left_tree if right_tree is None else right_tree

        # priority
        if left_tree[4] > right_tree[4]:
            left_tree[1] = self.merge(left_tree[1], right_tree)
            # return self.update(left)
            return left_tree
        else:
            right_tree[0] = self.merge(left_tree,right_tree[0])
            # return self.update(right)
            return right_tree


    # def node_size(self, node:Node):
    #     return 0 if node is None else node.count_partial
    
    # def node_key(self, node:None):
    #     return -1 if node is None else node.key

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

        if value <= node[3]:
            left_tree,right_tree = self.split(node[0], value)
            node[0] = right_tree
            return left_tree, node
        else:
            left_tree,right_tree = self.split(node[1], value)
            node[1] = left_tree
            return node, right_tree

    
    def insert(self, key:int,value:int =-1):
        value = value if value > 0 else key
        left_tree, right_tree = self.split(self.root, key)
        new_node = [None,None,key,value,random()]
        self.root = self.merge(self.merge(left_tree,new_node),right_tree)
    
    def erase(self, pos:int):
        middle_tree,right_tree = self.split(self.root, pos+1)
        left_tree,middle_tree = self.split(middle_tree, pos)
        self.root = self.merge(left_tree,right_tree)

        

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
        
    

    # def search(self, pos):
    #     #return self.search_recursively(pos,self.root)
    #     v = self.root
    #     while v:
    #         left_count = self.node_size(v.left)
    #         if pos < left_count:
    #             v = v.left
    #         elif pos == left_count:
    #             return v.value
    #         else:
    #             v = v.right
    #             pos -= left_count + 1
    #     return -1

    def search2(self, value):
        v = self.root
        upper = 10**18
        while v:
            if value == v[3]:
                return value

            elif value < v[3]:
                upper = v[3]
                v = v[0]
            else:
                v = v[1]
        return upper

    # def search_recursively(self, pos, node):
    #     if node is None:
    #         return -1
    #     num_left = 0 if node.left is None else node.left.count_partial
    #     if num_left + 1 == pos:
    #         return node.value
    #     if pos <= num_left:
    #         return self.search_recursively(pos, node.left)
    #     else:
    #         return self.search_recursively(pos - num_left - 1, node.right)
        


    
                










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