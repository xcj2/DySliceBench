def dicing(lis, inst):
    if inst == 'N':
        ans_lis = [lis[1],lis[5],lis[2],lis[3],lis[0],lis[4]]
    if inst == 'W':
        ans_lis = [lis[2],lis[1],lis[5],lis[0],lis[4],lis[3]]
    if inst == 'S':
        ans_lis = [lis[4],lis[0],lis[2],lis[3],lis[5],lis[1]]
    if inst == 'E':
        ans_lis = [lis[3],lis[1],lis[0],lis[5],lis[4],lis[2]]
    
    return(ans_lis)

def turn_right(lis):
    inst = list('ENW')
    for i in range(len(inst)):
        lis = dicing(lis, inst[i])
    return(lis)

def find_above(lis, num1, num2):
    inst1 = list('NNNEWW')
    for i in range(len(inst1)):
        if lis[0] == num1 and lis[5] == num2:
            break
        
        lis = dicing(lis, inst1[i])
        if lis[0] == num1 and lis[5] == num2:
            break
    return(lis)

def find_samedice(dice1,dice2):
    YN = 'No'
    lis = find_above(dice1, dice2[0], dice2[5])
    for i in range(4):
        lis = turn_right(lis)
        if lis == dice2:
            YN = 'Yes'
            break
    return(YN)

N = int(input())
dices = []
for i in range(N):
    dices.append(list(map(int, input().split())))

ans = 'Yes'
for i in range(N):
    for j in range(N):
        if i < j:
            if find_samedice(dices[i], dices[j]) == 'Yes':
                ans = 'No'

print(ans)
