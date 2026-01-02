A = [list(map(int,input().split())) for _ in range(3)]
ans = [[0]*3 for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]


for num in b:
    for i in range(3):
      for j in range(3):
          if A[i][j] == num:
             ans[i][j] = -1
             break

def f(ans):
    if yoko(ans) or tate(ans) or naname(ans):
        return True
    else:
        return False

def yoko(ans):
    tmp = []
    for i in ans:
        tmp.append(sum(i))
    if -3 in tmp:
        return True
    else:
        return False

def tate(ans):
    tmp = [0]*3
    for i in range(3):
        for j in range(3):
            tmp[j] += ans[i][j]
    if -3 in tmp:
        return True
    else:
        return False

def naname(ans):
    tmp = [0]*2
    tmp[0] = ans[0][0] + ans[1][1] + ans[2][2]
    tmp[1] = ans[0][2] + ans[1][1] + ans[2][0]
    if -3 in tmp:
        return True
    else:
        return False


if f(ans):
    print("Yes")
else:
    print("No")

