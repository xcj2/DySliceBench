S_a = list(input())
S_b = list(input())
S_c = list(input())

def a_turn(a, b, c):
    if len(a) == 0:
        print("A")
    elif a[0] == "a":
        a.pop(0)
        a_turn(a, b, c)
    elif a[0] == "b":
        a.pop(0)
        b_turn(a, b, c)
    elif a[0] == "c":
        a.pop(0)
        c_turn(a, b, c)

def b_turn(a, b, c):
    if len(b) == 0:
        print("B")
    elif b[0] == "a":
        b.pop(0)
        a_turn(a, b, c)
    elif b[0] == "b":
        b.pop(0)
        b_turn(a, b, c)
    elif b[0] == "c":
        b.pop(0)
        c_turn(a, b, c)

def c_turn(a, b, c):
    if len(c) == 0:
        print("C")
    elif c[0] == "a":
        c.pop(0)
        a_turn(a, b, c)
    elif c[0] == "b":
        c.pop(0)
        b_turn(a, b, c)
    elif c[0] == "c":
        c.pop(0)
        c_turn(a, b, c)

a_turn(S_a, S_b, S_c)