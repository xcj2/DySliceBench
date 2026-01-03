import sys

a, b, c = [list(input()) for _ in range(3)]

def A():
    if a == []:
        print("A")
        sys.exit()
    else:
        p = a.pop(0)
        if p == "a":
            A()
        elif p == "b":
            B()
        else:
            C()
            
def B():
    if b == []:
        print("B")
        sys.exit()
    else:
        p = b.pop(0)
        if p == "a":
            A()
        elif p == "b":
            B()
        else:
            C()
            
def C():
    if c == []:
        print("C")
        sys.exit()
    else:
        p = c.pop(0)
        if p == "a":
            A()
        elif p == "b":
            B()
        else:
            C()
            
A()