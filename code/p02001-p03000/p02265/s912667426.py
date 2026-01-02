class Node():
    def __init__(self,num,next=None,prev=None):
        self.num=num
        self.next=next
        self.prev=prev
class Doubly():
    def __init__(self):
        self.start=self.end=None
    def insert(self,x):
        it=Node(x)
        if self.end is None:
            self.end=self.start=it
        else:
            it.next=self.start
            self.start.prev=it
            self.start=it
    def delete(self,x):
        poin=self.start
        while(poin is not None):
            if poin.num==x:
                if poin.prev is None and poin.next is None:
                    self.start = self.end = None
                elif poin is self.start:#先頭
                    self.start.next.prev=None
                    self.start=poin.next
                elif poin is self.end:#末尾
                    poin.prev.next =None
                    self.end=poin.prev
                else:
                    poin.prev.next=poin.next
                    poin.next.prev=poin.prev
                break
            poin=poin.next
    # def deleteFirst(self):
    #     self.start=self.start.next
    # def deleteLast(self):
    #     self.end.prev.next =None
    #     self.end=self.end.prev
    def deleteFirst(self):
        if self.start is self.end:
            self.start = self.end = None
        else:
            self.start.next.prev = None
            self.start = self.start.next
    def deleteLast(self):
        if self.start is self.end:
            self.start = self.end = None
        else:
            self.end.prev.next = None
            self.end = self.end.prev
    def print(self):
        var=self.start
        lis=[]
        while var is not None:
            lis.append(var.num)
            var = var.next
        return ' '.join(lis)
from sys import stdin
N=int(input())
DB=Doubly()
# code=[input().split() for k in range(N)]
# for _ in range(N):
#     c=input().split()
#     if len(c)==1:
#         eval('DB.'+c[0]+'()')
#     else:
#         eval('DB.'+c[0]+'(c[1])')
for _ in range(N):
        cmd = stdin.readline().strip().split()
        if cmd[0] == 'insert':
            DB.insert(cmd[1])
        elif cmd[0] == 'delete':
            DB.delete(cmd[1])
        elif cmd[0] == 'deleteFirst':
            DB.deleteFirst()
        elif cmd[0] == 'deleteLast':
            DB.deleteLast()
print(DB.print())
