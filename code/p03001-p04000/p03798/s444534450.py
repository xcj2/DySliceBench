init_ts = ["SS", "SW", "WS", "WW"]

def notanim(t):
    if t=="S":
        return "W"
    else:
        return "S"

def nextAnimal(ts, s):
    if ts[1]=="S":
        if s=="o":
            return ts[0]
        else:
            return notanim(ts[0])
    elif ts[1]=="W":
        if s=="o":
            return notanim(ts[0])
        else:
            return ts[0]

def maket(n, s, init_t):
    t = init_t
    new_s = s[1:] + s[0]
    for i in range(n):
        t += nextAnimal(t[-2:], new_s[i])
    return t

n = int(input())
s = input()
flag = True
for init_t in init_ts:
    tmp_t = maket(n, s, init_t)
    if tmp_t[-2:]==init_t:
        print(tmp_t[:-2])
        flag = False
        break
    else:
        pass

if flag:
    print(-1)
