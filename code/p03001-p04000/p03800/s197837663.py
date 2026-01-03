def not_animal(animal):
    if animal == 'S':
        return 'W'
    return 'S'

def f(prev, animal, ans):
    x = g(animal, ans)
    if not x:
        return not_animal(prev)
    return prev

def g(animal, ans):
    ret = True
    if ans == 'x':
        ret = False

    if animal == 'S':
        return ret
    return not ret
    
def is_equal(x, y):
    return x == (y[0] == y[1])

N = int(input())
s = input()
circles = [['.' for i in range(N)] for i in range(4)]

_init = [('S', 'S'), ('W', 'W'),('S', 'W'), ('W', 'S')]

if s[0] == 'x':
    _init[:2], _init[2:] = _init[2:], _init[:2]

circles[0][0] = circles[1][0] = 'S'
circles[2][0] = circles[3][0] = 'W'

for i in range(4):
    circles[i][1], circles[i][-1] = _init[i]

for i in range(4):
    for j in range(1, N-2):
        circles[i][j+1] = f(circles[i][j-1], circles[i][j], s[j])
#    print(circles[i])


for i in range(4):
#    print(circles[i])
    for j in range(N):
#        print(g(circles[i][j], s[j]), circles[i][j-1], circles[i][(j+1)%N])
        if not is_equal(g(circles[i][j], s[j]), (circles[i][j-1], circles[i][(j+1)%N])):
            break
    else:
        print(''.join(circles[i]))
        break
else:
    print(-1)
