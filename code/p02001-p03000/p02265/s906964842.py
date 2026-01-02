from collections import deque
import sys

class doubly_linked_list():
    def __init__(self):
        #self.linked_list = []
        self.linked_list = deque([])
        #self.length = 0
    
    def insert(self, x):
        #self.linked_list.insert(0,x)
        self.linked_list.appendleft(x)
        #self.length += 1
    
    def delete(self, x):
        # 削除するのは、最初の要素だけでよい
        if x in self.linked_list:
            self.linked_list.remove(x)
            #self.length -= 1
    
    def delete_first(self):
        #if len(self.linked_list) != 0:
        #if self.length != 0:
            #self.linked_list.pop(0)
        self.linked_list.popleft()
            #self.length -= 1
    
    def delete_last(self):
        #if len(self.linked_list) != 0:
        #if self.length != 0:
            #self.linked_list.pop(self.length-1)
        self.linked_list.pop()
            #self.length -= 1

def get_method_and_run(cls, myinput):
    # 入力の受付
    #tmp = input()
    tmp = myinput().rstrip('\n')
    if tmp.find(" ") == -1:
        method = tmp
    else:
        method, x = tmp.split(" ")
    
    # 入力に従い、処理を実行
    if method == "insert":
        cls.insert(x)
    elif method == "delete":
        cls.delete(x)
    elif method == "deleteFirst":
        cls.delete_first()
    elif method == "deleteLast":
        cls.delete_last()
    else:
        pass

if __name__ == "__main__":
    myinput = sys.stdin.readline
    #n = int(input())
    n = int(myinput().rstrip('\n'))
    dll = doubly_linked_list()  
    [ get_method_and_run(dll, myinput) for i in range(n)]
    print(" ".join(dll.linked_list))


