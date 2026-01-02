def isneg(x):
    if x[0]=="-": return True
    else: return False


def neg(x):
    if isneg(x): return x[1:]
    else: return "-" + x

    
def zerot(x):
    rx = list(x[::-1])
    while rx[-1] == "0":
        rx.pop()
        if len(rx) == 0: 
            rx = ["0"]
            break
    return "".join(rx[::-1])


def zerocut(x):
    if isneg(x):
        ans = neg(zerot(neg(x)))
        if ans == "-0": return "0"
        return ans 
    else:
        return zerot(x)


def bigsmal(x, y):
    if isneg(x) or isneg(y): raise Exception("negative input")
    if len(x) > len(y):
        return x,y
    elif len(x) < len(y):
        return y,x
    else: return tuple(sorted([x, y])[::-1])
    
    
def bigsmall(x, y):
    if (not isneg(x)) and isneg(y):
        return x,y
    elif isneg(x) and (not isneg(y)):
        return y,x
    elif (not isneg(x)) and (not isneg(y)):
        return bigsmal(x, y)
    elif isneg(x) and isneg(y):
        tmp = bigsmal(neg(x), neg(y))[::-1]
        return tuple(neg(i) for i in tmp)
        
    
def ad(x, y):
    if isneg(x) or isneg(y): raise Exception("negative input")
    ra = [0] * (max(len(x), len(y)) + 1)
    rx = [int(i) for i in x][::-1]
    ry = [int(i) for i in y][::-1]
    for i in range(len(rx)): ra[i] += rx[i]
    for i in range(len(ry)): ra[i] += ry[i]
    for i in range(len(ra) - 1):
        ra[i+1] += ra[i] // 10
        ra[i] = ra[i] % 10
    ans = "".join([str(i) for i in ra][::-1])
    return zerocut(ans)


def s_b(x, y):
    if isneg(x) or isneg(y): raise Exception("negative input")
    if bigsmall(x, y) != (x, y): raise Exception("not x>=y error")
    ra = [0] * (max(len(x), len(y)))
    rx = [int(i) for i in x][::-1]
    ry = [int(i) for i in y][::-1]
    for i in range(len(rx)): ra[i] += rx[i]
    for i in range(len(ry)): ra[i] -= ry[i]
    for i in range(len(ra) - 1):
        if ra[i] < 0:
            ra[i] = 10 + ra[i]
            ra[i+1] -= 1
    ans = "".join([str(i) for i in ra][::-1])    
    return zerocut(ans)


def sb(x, y):
    if isneg(x) or isneg(y): raise Exception("negative input")
    if (x, y) == bigsmall(x, y):
        return s_b(x, y)
    else:
        return neg(s_b(y, x))


def add(x, y):
    if isneg(x) and isneg(y):
        return neg(ad(neg(x), neg(y)))
    elif (not isneg(x)) and (not isneg(y)):
        return ad(x, y)
    elif (not isneg(x)) and isneg(y):
        return sb(x, neg(y))
    elif isneg(x) and (not isneg(y)):
        return sb(y, neg(x))
    

def sub(x, y):
    if isneg(x) and isneg(y):
        return sb(neg(y), neg(x))
    elif (not isneg(x)) and (not isneg(y)):
        return sb(x, y)
    elif (not isneg(x)) and isneg(y):
        return ad(x, neg(y))
    elif isneg(x) and (not isneg(y)):
        return neg(ad(neg(x), y))
        

def ml(x, y):
    if isneg(x) or isneg(y): raise Exception("negative input")
    ra = [0] * (len(x) + len(y))
    rx = [int(i) for i in x][::-1]
    ry = [int(i) for i in y][::-1]
    for i in range(len(rx)):
        for j in range(len(ry)):
            ra[i+j] += rx[i] * ry[j]
    for i in range(len(ra) - 1):
        ra[i+1] += ra[i] // 10
        ra[i] = ra[i] % 10
    ans = "".join([str(i) for i in ra][::-1])
    return zerocut(ans)
    

def mul(x, y):
    if isneg(x) and isneg(y):
        return ml(neg(y), neg(x))
    elif (not isneg(x)) and (not isneg(y)):
        return ml(x, y)
    elif (not isneg(x)) and isneg(y):
        return neg(ml(x, neg(y)))
    elif isneg(x) and (not isneg(y)):
        return neg(ml(neg(x), y))
        

def mod2(x):
    return int(x[-1]) % 2


def div2(x):
    if isneg(x): raise Exception("negative input")
    ans = [0] * len(x)
    xs = [int(i) for i in x]
    for i in range(len(x)-1):
        ans[i] += xs[i]
        ans[i+1] += (ans[i]%2) * 10
        ans[i] //= 2
    ans[len(x)-1] = (ans[len(x)-1] + xs[len(x)-1])//2
    ans = "".join([str(i) for i in ans])
    return zerocut(ans)


n = input()
even = div2(n)
odd = sub(n, even)
print(mul(even, odd))