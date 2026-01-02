words = "a b c d e f g h i j k l m n o p q r s t u v w x y z ".split()

def calcMax(current, i):
    maxC = -1
    for c in range(N):
        if(c != N - i):
            maxC = max(maxC, current[c])
    return maxC

def seek(current):
    for i in range(1, N):
        if(current[-i] <= max(current[:-i])):
            current[-i] += 1
            for j in range(i-1):
                current[N-1-j] = 0
            return True, current
    return False, current

def convert(ans):
    ansStr = ""
    for a in ans:
        ansStr += words[a]
    return ansStr

N = int(input())

ans = [0] * N

print(convert(ans))
flag, ans = seek(ans)
while(flag == True):
    print(convert(ans))
    flag, ans = seek(ans)