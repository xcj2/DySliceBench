def spaceinput():
    return list(map(int, input().split(" ")))

def count3(S, l, r):
    for i in range(l, r+1):
        if S[i:i+3] == "...":
            return True
    return False

def is_twocontinusblock(S, l, r):
    for i in range(l,r+1):
        if S[i:i+2] == "##":
            return True
    return False


N, A, B, C, D = spaceinput()
S = input()
S="A"+S
#print(S)
def solve():
    if is_twocontinusblock(S, A, C-1) or is_twocontinusblock(S, B, D-1):
        return False
    if D < C:
        if count3(S, B-1, D-1):
            return True
        else:
            return False

    return True


if solve():
    print("Yes")
else:
    print("No")





