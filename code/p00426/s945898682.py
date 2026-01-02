def move(a,b):
    aa = a[:]
    bb = b[:]
    bb.append(aa.pop(-1))
    return aa,bb

def move_is_True(a,b):
    if len(a) == 0:
        return False
    elif len(b) == 0 or a[-1]>b[-1]:
        return True
    return False

def search(abc_first, n):
    counts = [10**10]
    abcs = [(abc_first, abc_first, 0)]
    while True:
        if len(abcs) == 0 or min(counts) < sorted(abcs, key=lambda x:x[2])[0][2]:
            break
        new_abcs = []
        for abc, last_abc, count in abcs:
            abc_copy = abc[:]
            #print("abc", abc)
            a = abc_copy[0]
            b = abc_copy[1]
            c = abc_copy[2]
            if len(a) == n or len(c) == n:
                counts.append(count)
            else:
                movements = [(a,b), (b,a), (c,b), (b,c)]
                can_move = [move_is_True(a,b) for a,b in movements] #a2b, b2a, c2b, b2c
                #print("can_move", can_move)
                for i in range(4):
                    if can_move[i]:
                        new_count = count+1
                        x,y = movements[i]
                        x,y = move(x,y)
                        if i == 0:
                            new_abc = [x,y,c]
                        elif i == 1:
                            new_abc = [y,x,c]
                        elif i == 2:
                            new_abc = [a,y,x]
                        elif i == 3:
                            new_abc = [a,x,y]
                        #print(abc, new_abc, new_count, n)
                        if new_abc != last_abc:
                            if new_count < 15000000:
                                new_abcs.append((new_abc, abc, new_count))
            abcs = new_abcs[:]
    return min(counts)

n, m = map(int, input().split())
while (m!=0 or n!=0):
    abc = []
    for i in range(3):
        abc.append(list(map(int, input().split()))[1:])
    ans = search(abc, n)
    if ans <= m:
        print(ans)
    else:
        print(-1)
    n, m = map(int, input().split())

