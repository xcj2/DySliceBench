N = int(input())
t = list(input())
Ans = ['n' for _ in t]
 
def judge(prevSW, SW, ox):
    if SW == 'S':
        if ox == 'o':
            return prevSW
        else:
            if prevSW == 'S':
                return 'W'
            else: return 'S'
    elif SW == 'W':
        if ox == 'x':
            return prevSW
        else:
            if prevSW == 'S':
                return 'W'
            else: return 'S'
 
def decideorder(startSW):
    Ans[1] = startSW
    for i in range(2,N):
        Ans[i] = judge(Ans[i-2], Ans[i-1], t[i-1])

def check():
    if judge(Ans[-2], Ans[-1], t[-1]) is Ans[0] and judge(Ans[-1], Ans[0], t[0]) is Ans[1]:
        return True
    else:
        return False

Ans[0] = 'S'
decideorder('S')
if check():
    print("".join(Ans))
else:
    decideorder('W')
    if check():
        print("".join(Ans))
    else:
        Ans[0] = 'W'
        decideorder('S')
        if check():
            print("".join(Ans))
        else:
            decideorder('W')
            if check():
                print("".join(Ans))
            else:
                print(-1)