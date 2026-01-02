dice = list(map(int, input().split()))
q = int(input())

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

def find_above(lis, num):
    inst1 = list('NNNEWW')
    for i in range(len(inst1)):
        if lis[0] == num:
            break
        
        lis = dicing(lis, inst1[i])
        if lis[0] == num:
            break
    return(lis)

for i in range(q):
    question = list(map(int, input().split()))
    lis = [1,2,3,4,5,6]
    lis = find_above(lis, dice.index(question[0]) + 1)
    for j in range(4):
        lis = turn_right(lis)
        if dice[lis[1]- 1] == question[1]:
            break

    print(dice[lis[2]-1])
