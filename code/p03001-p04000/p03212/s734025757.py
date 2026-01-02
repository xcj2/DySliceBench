import itertools

n_s = input()
keta = len(n_s)
n = int(n_s)
count = 0

def list_753(n):
    l = list(itertools.product((7, 5, 3), repeat=n))
    ans = []
    for x in l:
        numstr = ''
        for i in range(n):
            numstr += str(x[i])
        ans.append(int(numstr))
    return sorted(ans)

def howmany_753(n):
    return ((3 ** n) - (3 * (2 ** n - 2)) - 3)

def judge_753(n):
    s = str(n)
    if s.count('7') * s.count('5') * s.count('3') != 0:
        return True
    else:
        return False

for i in range(3, keta):
    count += howmany_753(i)

numlist = list_753(keta)
for x in numlist:
    if x <= n:
        if judge_753(x) == True:
            count += 1
    else:
        break
print(count)