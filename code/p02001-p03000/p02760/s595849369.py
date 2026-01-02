C = []
result = [[0]*3 for i in range(3)]
ans = "No"
for i in range(3):
    a = list(map(int, input().split()))
    C.append(a)

def check():
    b = int(input())
    for i in range(3):
        for j in range(3):
            a = C[i][j]
            if b == a:
                result[i][j] = 1

def column():
    for j in range(3):
        for i in range(3):
            if result[i][j] == 0:
                break
        else:
            global ans
            ans = "Yes"

def row():
    for i in range(3):
        for j in range(3):
            if result[i][j] == 0:
                break
        else:
            global ans
            ans = "Yes"

def naname():
    global ans
    for j in range(3):
        if result[j][j] == 0:
            break
    else:
        ans = "Yes"
    for j in range(3):
        if result[j][2-j] == 0:
            break
    else:
        ans = "Yes"

N = int(input())
for i in range(N):
    check()
    column()
    row()
    naname()

print(ans)
