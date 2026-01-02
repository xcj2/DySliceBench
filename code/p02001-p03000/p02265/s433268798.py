class Element:
    def __init__(self, x):
        self.x = x
        self.lh = None
        self.rh = None

class MyDeque:
    def __init__(self):
        self.top = self.tail = None
    
    def insert(self, x):
        elm = Element(x)
        if self.top is None:
            self.top = self.tail = elm
        else:
            elm.rh = self.top
            self.top.lh = self.top = elm
        
    def delete(self, x):
        elm = self.top
        while elm is not None:
            if elm.x == x:
                if elm.lh is None and elm.rh is None:
                    self.top = self.tail = None
                else:    
                    if elm.lh is None:
                        self.top = elm.rh
                    else:
                        elm.lh.rh = elm.rh
                        
                    if elm.rh is None:
                        self.tail = elm.lh
                    else:
                        elm.rh.lh = elm.lh
                break
            
            elm = elm.rh
            
    def delete_first(self):
        if self.top is self.tail:
            self.top = self.tail = None
        else:
            self.top = self.top.rh
            self.top.lh = None
                
    def delete_last(self):
        if self.top is self.tail:
            self.top = self.tail = None
        else:
            self.tail = self.tail.lh
            self.tail.rh = None
                
    
    def print_que(self):
        elm = self.top
        q=[]
        while elm is not None:
            q.append(elm.x)
            elm = elm.rh
        print(*q)

from sys import stdin

que = MyDeque()
N = int(input())
for _ in range(N):
    cmd = stdin.readline().strip().split()
    if cmd[0] == 'insert':
        que.insert(cmd[1])
        #que.print_que()        
        
    elif cmd[0] == 'delete':
        que.delete(cmd[1])
        #que.print_que()
        
    elif cmd[0] == 'deleteFirst':
        que.delete_first()
        #que.print_que()
        
    elif cmd[0] == 'deleteLast':
        que.delete_last()
        #que.print_que()
    
que.print_que()
