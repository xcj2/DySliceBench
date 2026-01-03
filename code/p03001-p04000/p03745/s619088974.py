def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()

cnt = 1
state = 'first'
for i in A:
#    print(i)
    if state == 'first':
        state = 'even'
    else:
        if state == 'even':
            if i > num:
                state = 'more'
            elif i < num:
                state = 'less'
        elif state == 'more':
            if i < num:
                cnt += 1
                state = 'even'
        elif state == 'less':
            if i > num:
                cnt += 1
                state = 'even'
    num = i
#print((cnt,state))
print(cnt)