n = int(input())
s = input()

def acceptable(ary):
    flag = True
    if ary[0]:
        if s[0] == 'o':
            flag = ary[1] == ary[-1]
        else:
            flag = ary[1] != ary[-1]
    else:
        if s[0] == 'x':
            flag = ary[1] == ary[-1]
        else:
            flag = ary[1] != ary[-1]
    if ary[-1]:
        if s[-1] == 'o':
            flag = flag and ary[0] == ary[-2]
        else:
            flag = flag and ary[0] != ary[-2]
    else:
        if s[-1] == 'x':
            flag = flag and ary[0] == ary[-2]
        else:
            flag = flag and ary[0] != ary[-2]
    return flag

def solve(ary):
    for i in range(1, n-1):
        if ary[i]:
            if s[i] == 'o':
                ary.append(ary[i-1])
            else:
                ary.append(not ary[i-1])
        else:
            if s[i] == 'x':
                ary.append(ary[i-1])
            else:
                ary.append(not ary[i-1])
    return ary

def print_ans(ans):
    print(''.join(['S' if a else 'W' for a in ans]))

for t in ([True, True], [True, False], [False, True], [False, False]):
    ans = solve(t)
    if acceptable(ans):
        print_ans(ans)
        exit()
print(-1)
