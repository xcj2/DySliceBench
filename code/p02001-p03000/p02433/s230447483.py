class Node:
    def __init__(self, val=None, prev=None, nextNode=None):
        self.val = val
        self.prev = prev
        self.nextNode = nextNode

class LinkedList():
    def __init__(self):
        self.end = Node('END')
        self.cursol_node = self.end
    
    def insertBefore(self, x):
        new_node = Node(val=x, prev=self.cursol_node.prev, nextNode=self.cursol_node)
        if self.cursol_node.prev != None:
            self.cursol_node.prev.nextNode = new_node
        #現在のカーソルノードのprevを新しいノードとリンク
        self.cursol_node.prev = new_node
        #新しいノードをカーソルノードとする
        self.cursol_node = new_node

    def move(self, d):
        if d > 0:
            for i in range(d):
                #ノードのnextがENDになるまでカーソルノードを移動
                if self.cursol_node.nextNode == None:break
                self.cursol_node = self.cursol_node.nextNode
        elif d < 0:
            for i in range(abs(d)):
                if self.cursol_node.prev == None:break
                self.cursol_node = self.cursol_node.prev

    def erase(self):
        if self.cursol_node != self.end:
            if self.cursol_node.prev != None:
                #前提条件としてcursolがENDにある状態でeraseは行われないため、prevのみNoneチェック
                self.cursol_node.prev.nextNode = self.cursol_node.nextNode
            self.cursol_node.nextNode.prev = self.cursol_node.prev
            self.cursol_node = self.cursol_node.nextNode
    
    def print_nodes_val(self):
        ans_list = []
        target_node = self.end
        while True:
            if target_node.prev == None:break
            else:
                target_node = target_node.prev
                ans_list.append(target_node.val)
        ans_list = ans_list[::-1]
        return ans_list

linkedList = LinkedList()
n = int(input())
for i in range(n):
    q,*x = map(int, input().split())
    x = x[0] if x else None
    if q == 0:
        linkedList.insertBefore(x)
    elif q == 1:
        linkedList.move(x)
    elif q == 2:
        linkedList.erase()
print('\n'.join(map(str,linkedList.print_nodes_val())))

