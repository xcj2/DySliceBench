def addleave(p):
    for i in range(1, n-1):
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
    if check(result):
        return result
    result = addleave("SW")
    if check(result):
        return result
    result = addleave("WS")
    if check(result):
        return result
    result = addleave("WW")
    if check(result):
        return result
    return -1

def check(res):
    flag = True
    for i in range(n):
        if res[(i + n - 1) % n] == res[(i + n + 1) % n] and res[i]=="S" and s[i]=="o":
            pass
        elif res[(i + n - 1) % n] != res[(i + n + 1) % n] and res[i]=="S" and s[i]=="x":
            pass
        elif res[(i + n - 1) % n] == res[(i + n + 1) % n] and res[i]=="W" and s[i]=="x":
            pass
        elif res[(i + n - 1) % n] != res[(i + n + 1) % n] and res[i]=="W" and s[i]=="o":
            pass
        else:
            flag = False
    return flag
if __name__=="__main__":
    n = int(input())
    s = input()
    print(solve())