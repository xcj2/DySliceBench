import sys
input = sys.stdin.readline
#MAX_ARRAY_SIZE = 10**6

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.prev = None
        self.next = None

nil = Node(None)

#class DoublyLinkedList:
#    global nil
def init():
    nil.next = nil
    nil.prev = nil

def insert(x):
    node = Node(x)
    # 番兵の直後に要素を追加
    node.next = nil.next
    nil.next.prev = node
    nil.next = node
    node.prev = nil

def delete(x):
    # 検索したノードを削除
    deleteNode(listSearch(x))

def deleteFirst():
    deleteNode(nil.next)

def deleteLast():
    deleteNode(nil.prev)

def deleteNode(node):
    # nodeが番兵の場合は処理をしない
    if node is nil:
        return
    node.prev.next = node.next
    node.next.prev = node.prev
    del node

def listSearch(x):
    # 番兵の次の要素から辿る
    cur = nil.next
    while cur is not nil and cur.data != x:
        cur = cur.next
    return cur

#double_list = DoublyLinkedList()
init()

N = int(input())
for i in range(N):
    command = input().strip().split()
    if command[0] == 'deleteFirst':
        deleteFirst()
    elif command[0] == 'deleteLast':
        deleteLast()
    elif command[0] == 'delete':
        delete(command[1])
    elif command[0] == 'insert':
        insert(command[1])

while nil.next is not nil:
    if nil.next.next is not nil:
        print(nil.next.data, end=" ")
    else:
        print(nil.next.data)
    nil.next = nil.next.next
