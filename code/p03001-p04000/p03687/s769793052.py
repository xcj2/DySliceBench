def ope(s,c):
    ret = ""
    for i in range(len(s)-1):
        if s[i] == c or s[i+1] == c:
            ret += c
        else:
            ret += s[i]
    return ret

def is_filled(s,c):
    for i in s:
        if i != c:
            return False
    else:
        return True

def main():
    s = input()
    ans = 114514
    for i in range(97,97+26):
        c = chr(i)
        if not c in s: continue
        si = s

        turn = 0
        while not is_filled(si,c):
            si = ope(si,c)
            turn += 1
        
        ans = min(ans,turn)
    print(ans)

        
main()
