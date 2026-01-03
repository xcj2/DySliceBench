def isOdd(n):
    return n % 2 == 1


def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


A, B, C = li()

cnt = 0
ABC = []
flag = False
while True:
    if flag:
        break
    if isOdd(A) or isOdd(B) or isOdd(C):
        break
    ABC.append([A, B, C])
    A2 = A // 2
    B2 = B // 2
    C2 = C // 2
    A = B2 + C2
    B = A2 + C2
    C = A2 + B2
    cnt += 1

    for i in range(len(ABC)):
        if ABC[i] == [A, B, C]:
            cnt = -1
            flag = True
            break

print(cnt)
