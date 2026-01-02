h, w = map(int, input().split())

p = list(range(h*w))

def find(x):
    global p
    if p[x] == x:return x
    p[x] = find(p[x])
    return p[x]

def unite(x, y):
    global p
    x = find(x)
    y = find(y)
    if x != y:p[x] =y

def real_number(i, j):
    i += 1
    j += 1
    i %= 4
    j %= 4
    if i == 1 and j == 1:return 6
    if i == 1 and j == 2:return 3
    if i == 1 and j == 3:return 1
    if i == 1 and j == 0:return 4
    if i == 2 and j == 1:return 2
    if i == 2 and j == 3:return 2
    if i == 3 and j == 1:return 1
    if i == 3 and j == 2:return 3
    if i == 3 and j == 3:return 6
    if i == 3 and j == 0:return 4
    if i == 0 and j == 1:return 5
    if i == 0 and j == 3:return 5
    return -1
    
field = [input() for i in range(h)]
for i in range(h):
    for j in range(w):
        if str(real_number(i,j)) != field[i][j]:continue
        if i + 1 < h and str(real_number(i+1,j)) == field[i+1][j]:
            unite(i*w+j, (i+1)*w+j)
        if j + 1 < w and str(real_number(i,j+1)) == field[i][j+1]:
            unite(i*w+j, i*w+j+1)

if find(0) == find(h*w-1):
    print("YES")
else:
    print("NO")
    
        
