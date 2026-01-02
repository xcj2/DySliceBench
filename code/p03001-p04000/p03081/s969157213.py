[N,Q] = list(map(int,input().split()))
s = str(input())
magic = [input().split() for j in range(Q)]

def move_golem(ini,s,magic):
    golem_temp = ini
    for t,d in magic:
        if s[golem_temp] == t:
            if d == 'L':
                golem_temp -= 1
            elif d == 'R':
                golem_temp += 1
        if golem_temp == -1 or golem_temp == len(s):
            break
    return golem_temp

# check lower bound

def check_lower(s,magic):
    lb = -1
    ub = len(s)
    while ub - lb > 1:
        mid = (lb + ub)//2
        mid_golem_temp = move_golem(mid,s,magic)
        if mid_golem_temp == -1:
            lb = mid
        elif mid_golem_temp != -1:
            ub = mid
            
    return lb

def check_upper(s,magic):
    lb = -1
    ub = len(s)
    while ub - lb > 1:
        mid = (lb + ub)//2
        mid_golem_temp = move_golem(mid,s,magic)
        if mid_golem_temp == len(s):
            ub = mid
        elif mid_golem_temp != len(s):
            lb = mid
            
    return ub

print(check_upper(s,magic)-check_lower(s,magic)-1)