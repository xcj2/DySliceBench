N = int(input())
n = len(str(N))

cnt = 0
for i in range(3,n+1):
    l = []
    x = ""
    def fa(x,l,i):
        if len(x) == i:
            if int(x) <= N:
                if x.count("3") >= 1 and x.count("5") >= 1 and x.count("7"):
                    l.append(x)
            return 
        else:
            x += "3"
            fa(x,l,i)
            fb(x,l,i)
            fc(x,l,i)
    def fb(x,l,i):
        if len(x) == i:
            if int(x) <= N:
                if x.count("3") >= 1 and x.count("5") >= 1 and x.count("7"):
                    l.append(x)
            return 
        else:
            x += "5"
            fa(x,l,i)
            fb(x,l,i)
            fc(x,l,i)
    def fc(x,l,i):
        if len(x) == i:
            if int(x) <= N:
                if x.count("3") >= 1 and x.count("5") >= 1 and x.count("7"):
                    l.append(x)
            return 
        else:
            x += "7"
            fa(x,l,i)
            fb(x,l,i)
            fc(x,l,i)
    fa(x,l,i)
    fb(x,l,i)
    fc(x,l,i)
    k = sorted(set(l))
    cnt += len(k)

print(cnt)