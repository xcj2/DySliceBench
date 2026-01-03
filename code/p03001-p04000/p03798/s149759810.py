n = int(input())
s = input()

def addleave(p):
    for i in range(1,n):
        if s[i]=="o":
            if p[i]=="S":
                p += "S" if p[i-1]=="S" else "W"
            else:
                p += "W" if p[i-1]=="S" else "S"
        else:
            if p[i]=="S":
                p += "W" if p[i-1]=="S" else "S"
            else:
                p += "S" if p[i-1]=="S" else "W"
    return p
def solve():
    result = addleave("SS")
    if result[-1] == result[0]:
        if check(result):
            return result[:-1]
    result = addleave("SW")
    if result[-1] == result[0]:
        if check(result):
            return result[:-1]
    result = addleave("WS")
    if result[-1] == result[0]:
        if check(result):
            return result[:-1]

    result = addleave("WW")
    if result[-1] == result[0]:
        if check(result):
            return result[:-1]
    return -1

def check(res):
    res = res[:-1] + res[:-1] + res[:-1]
    flag = True
    for i in range(n):
        if res[n + i - 1] == res[n + i + 1] and res[n + i]=="S" and s[i]=="o":
            pass
        elif res[n + i - 1] != res[n + i + 1] and res[n + i]=="S" and s[i]=="x":
            pass
        elif res[n + i - 1] == res[n + i + 1] and res[n + i]=="W" and s[i]=="x":
            pass
        elif res[n + i - 1] != res[n + i + 1] and res[n + i]=="W" and s[i]=="o":
            pass
        else:
            flag = False
    return flag
print(solve())