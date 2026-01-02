from random import random
class Node:
        def __init__(self, key, value:int=-1):
            self.left = None
            self.right = None
            self.key = key
            self.value = value
            self.priority = int(random()*10**7)
            # self.count_partial = 1
            self.sum_partial = value

 

class Treap:
    
    #Node [left, right, key, value, priority, num_partial, sum_partial]
    def __init__(self):
        self.root = None

    def update(self, node) -> Node:
        if node.left is None:
            # left_count = 0
            left_sum = 0
        else:
            # left_count = node.left.count_partial
            left_sum = node.left.sum_partial
        if node.right is None:
            # right_count = 0
            right_sum = 0
        else:
            # right_count = node.right.count_partial
            right_sum = node.right.sum_partial

        # node.count_partial = left_count + right_count + 1
        node.sum_partial = left_sum  + node.value + right_sum
        return node

    def merge(self, left :Node, right:Node):
        if left is None or right is None:
            return left if right is None else right

        if left.priority > right.priority:
            left.right = self.merge(left.right,right)
            return self.update(left)
        else:
            right.left = self.merge(left,right.left)
            return self.update(right)


    # def node_size(self, node:Node) -> int:
    #     return 0 if node is None else node.count_partial
    
    def node_key(self, node: Node) -> int:
        return -1 if node is None or node.key is None else node.key
    
    def node_sum(self, node: Node) -> int:
        return 0 if node is None else node.sum_partial

    #指定された場所のノードは右の木に含まれる
    def split(self, node:None, key:int) -> (Node, Node):
        if node is None:
            return None,None
        if key <= self.node_key(node):
            left,right = self.split(node.left, key)
            node.left = right
            return left, self.update(node)
        else:
            left,right = self.split(node.right, key)
            node.right = left
            return self.update(node),right

    
    def insert(self, key:int, value:int =-1):
        value = value if value > 0 else key
        left, right = self.split(self.root, key)
        new_node = Node(key,value)
        self.root = self.merge(self.merge(left,new_node),right)
    
    def erase(self, key:int):
        # print('erase pos=',pos,'num=',self.search(pos),'num_nodes=',self.root.count_partial)
        middle,right = self.split(self.root, key+1)
        # print(middle.value if middle is not None else -1,middle.count_partial if middle is not None else -1,right.value if right is not None else -1,right.count_partial if right is not None else -1)
        left,middle = self.split(middle, key)
        # print(left.value if left is not None else -1,left.count_partial if left is not None else -1, middle.value if middle is not None else -1,middle.count_partial if middle is not None else -1,)
        self.root = self.merge(left,right)


    def printTree(self, node=None, level=0):
        node = self.root if node is None else node
        if node is None:
            print('level=',level,'root is None')
            return
        else:
            print('level=',level,'k=',node.key,'v=',node.value, 'p=',node.priority)
        if node.left is not None:
            print('left')
            self.printTree(node.left,level+1)
        
        if node.right is not None:
            print('right')
            self.printTree(node.right,level+1)
        
    

    def find(self, key):
        #return self.search_recursively(pos,self.root)
        v = self.root
        while v:
            v_key = self.node_key(v)
            if key == v_key:
                return v.value
            elif key < v_key:
                v = v.left
            else:
                v = v.right
        return -1
    def interval_sum(self, left_key, right_key):
        lt_left, ge_left = self.split(self.root,left_key)
        left_to_right, gt_right = self.split(ge_left, right_key + 1)
        res = self.node_sum(left_to_right)
        self.root = self.merge(lt_left, self.merge(left_to_right, gt_right))
        return res



def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    N,D,A = LMIIS()
    enemies = []
    for i in range(N):
        x, h = LMIIS()
        enemies.append((x, ceil(h/A)))
    enemies.sort()
    bomb = Treap()
    ans = 0
    for i, (x, h) in enumerate(enemies):
        left = x - D
        right = x + D
        remain_h = h - bomb.interval_sum(left, right)
        if remain_h <= 0:
            continue

        ans += remain_h
        bomb.insert(x + D, remain_h)
    print(ans)
        





    
main()