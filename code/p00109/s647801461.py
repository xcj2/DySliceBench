
def solve(s):

    def expr(l):
        left, mid = term(l)
        return edum(mid, left)
    
    def edum(l, lval):
        if s[l] == '+':
            val, mid = term(l + 1)
            return edum(mid, lval + val)
        if s[l] == '-':
            val, mid = term(l + 1)
            return edum(mid, lval - val)
        else:
            return lval, l
    
    def term(l):
        left, mid = value(l)
        return tdum(mid, left)

    def tdum(l, lval):
        if s[l] == '*':
            l += 1
            val1, mid = value(l)
            return tdum(mid, lval * val1)
        if s[l] == '/':
            l += 1
            val1, mid = value(l)
            return tdum(mid, (abs(lval) // abs(val1)) * (-1 if (lval < 0) ^ (val1 < 0) else 1))
        else:
            return lval, l

    def value(l):
        if s[l] == '(':
            val1, mid = expr(l + 1)
            return val1, mid + 1
        else:
            val = 0
            fl =  s[l] == '-'
            if fl:
                l += 1
            while s[l].isdecimal():
                val *= 10
                val += int(s[l])
                l += 1
            if fl:
                val *= -1
            return val, l

    res = expr(0)[0]
    """
    gnd = eval(''.join(s[:-1]).replace('/', '//'))
    while res != gnd:
        pass
    """
    print(res)

def main():
    q = int(input())
    for _ in range(q):
        solve(list(input()))

if __name__ == '__main__':
    main()
