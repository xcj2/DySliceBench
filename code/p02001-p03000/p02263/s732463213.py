class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, d):
        new = Cell(d)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            print('Stack Under Flow!!')
            return
        else:
            t = self.top.value
            p = self.top
            self.top = self.top.next
            del(p)
            return t

l = list(input().split())
st = Stack()
for i in l:
    if i == '-':
        t1 = st.pop()
        t2= st.pop()
        st.push(t2-t1)
    elif i=='*':
        t1 = st.pop()
        t2= st.pop()
        st.push(t1*t2)
    elif i == '+':
        t1 = st.pop()
        t2 = st.pop()
        st.push(t1 + t2)
    else:
        st.push(int(i))
print(st.pop())

