def another(t):
    if t == "W":
        return "S"
    else:
        return "W"


def ok(t1, t2, t3, op):
    if (op == "o" and t2 == "S") or (op == "x" and t2 == "W"):
        return t1 == t3
    else:
        return t1 != t3

def check(ans):
    for i in range(n - 2):
        c = s[i]
        t = ans[i]
        if (c == "o" and t == "S") or (c == "x" and t == "W"):
            ans[i + 1] = ans[i - 1]
        else:
            ans[i + 1] = another(ans[i - 1])
    t1, t2, t3, t4 = ans[-3], ans[-2], ans[-1], ans[0]
    return ok(t1, t2, t3, s[-2]) and ok(t2, t3, t4, s[-1])

n = int(input())
s = input()

for head, tail in (("S", "S"), ("S", "W"), ("W", "S"), ("W", "W")):
    ans = [""] * n
    ans[0] = head
    ans[-1] = tail
    if check(ans):
        print(*ans, sep="")
        break
else:
    print(-1)
