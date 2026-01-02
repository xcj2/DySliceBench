def RL(a):
    if a=='R':
        return 1
    elif a=='L':
        return -1
    else:
        return 0
    
def UD(a):
    if a=='D':
        return 1
    elif a=='U':
        return -1
    else:
        return 0

def printLim(minus_lim, plus_lim, MAX):
    if minus_lim <0:
        print('X|', end='')
    else:
        print('|'+'X'*(minus_lim+1), end='')
    
    print('O'*(plus_lim - minus_lim -1), end='')
    if plus_lim ==MAX:
        print('|X')
    else:
        print('X'*(MAX-plus_lim) + '|')

def isFall(s_data,t_data,MAX,target):
    a = -1
    b = MAX
    for i in range(N-1, -1,-1):
        save = t_data[i]
        if save == 1:
            a-=1
        elif save == -1:
            b+=1
            
        # limit check
        if a < -1:
            a=-1
        if b>MAX:
            b=MAX
        if a==b:
            break
#         printLim(a,b,MAX)

        kill = s_data[i]
#         print(kill, save)
        # A lim
        if kill == -1:
            a +=1
        # B lim
        elif kill == 1:
            b -=1

        # limit check
        if a < -1:
            a=-1
        if b>MAX:
            b=MAX
        if (b-a) ==1:
            break


#         printLim(a,b,MAX)
#     print(a,b)
    
    if a < target < b:
        return False
    else:
        return True




################
H, W, N = map(int,input().split())
orig_y,orig_x = map(int,input().split())
orig_y -=1
orig_x -=1
s = input()
t = input()


flag = isFall([RL(it) for it in s],[RL(it) for it in t],W,orig_x)
flag |= isFall([UD(it) for it in s],[UD(it) for it in t],H,orig_y)
if flag:
    print('NO')
else:
    print('YES')