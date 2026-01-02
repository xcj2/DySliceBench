def biserch(l,key,flag=True):
    if flag is True:
        func = judge_1
    else:
        func = judge_2
    left = -1; right = len(l)
    while right - left > 1:
        middle = (left+right) // 2
        if func(l,key,middle) is True:
            right = middle
        else:
            left = middle
    return right

def judge_1(l,key,middle):
    if key <= l[middle]:
        return True
    else:
        return False

def judge_2(l,key,middle):
    if key < l[middle]:
        return True
    else:
        return False

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

ans = 0
for b in B:
    top = biserch(A,b)
    bottom = N - biserch(C,b,flag=False)
    ans += top*bottom
print(ans)