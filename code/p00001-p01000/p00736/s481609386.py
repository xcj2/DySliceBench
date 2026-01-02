from collections import deque


def AND(a, b):
    if a == "0" or b == "0":
        return "0"
    elif a == b == "2":
        return "2"
    else:
        return "1"


def OR(a, b):
    if a == "2" or b == "2":
        return 2
    elif a == b == "0":
        return "0"
    else:
        return "1"


def NOT(a):
    if a.count("-") % 2 == 1:
        if a[0] == "0":
            return "2"
        elif a[0] == "2":
            return "0"
        else:
            return "1"
    else:
        return a[0]


def solve(S):
    que = deque()
    for s in S:
        if s == ")":
            formula = ""
            while True:
                q = que.pop()
                if q == "(":
                    break
                formula += q
            if "+" in formula:
                a, b = formula.split("+")
                a = NOT(a)
                b = NOT(b)
                que.append(str(OR(a, b)))
            if "*" in formula:
                a, b = formula.split("*")
                a = NOT(a)
                b = NOT(b)
                que.append(str(AND(a, b)))
        else:
            que.append(s)
    return NOT("".join(reversed(que)))


while True:
    S = input()
    if S == ".":
        break
    count = 0
    for p in range(3):
        for q in range(3):
            for r in range(3):
                if solve(S.replace("P", str(p)).replace("Q", str(q)).replace("R", str(r))) == "2":
                    count += 1
    print(count)
