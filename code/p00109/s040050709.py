def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

# Convert String to List
def String2List(s):
    L = []; tmp = ""
    for i in s:
        if i.isdigit():
            tmp += i
        else:
            if tmp != "":
                L.append(tmp)
                tmp = ""
            L.append(i)
    if tmp != "":
        L.append(tmp)

    return L

# generate Reverse Polish Notation
def Generate_RPN(L):
    S, L2 = [], []
    table = {"*": 1, "/": 1, "+": 0, "-": 0, "(": -1, ")": -1}
    for i in L:
        if i.isdigit():
            L2.append(i)
        elif i == "(":
            S.append(i)
        elif i == ")":
            while S[-1] != "(":
                L2.append(S.pop())
            S.pop()
        else:
            while len(S) != 0 and (table[S[-1]] >= table[i]):
                L2.append(S.pop())
            S.append(i)

    while len(S) != 0:
        L2.append(S.pop())

    return L2

Nline = int(input())
for ll in range(Nline):

    S = input()
    p = Generate_RPN(String2List(S[0:-1]))
    N = len(p)

    s = []
    for i in range(len(p)):
        if p[i] == "+":
            a = int(s.pop())
            b = int(s.pop())
            s.append(str(b+a))
        elif p[i] == "-":
            a = int(s.pop())
            b = int(s.pop())
            s.append(str(b-a))
        elif p[i] == "*":
            a = int(s.pop())
            b = int(s.pop())
            s.append(str(b*a))
        elif p[i] == "/":
            a = int(s.pop())
            b = int(s.pop())
            s.append(str(int(b/a)))
        else:
            s.append(p[i])
    print(s[0])

