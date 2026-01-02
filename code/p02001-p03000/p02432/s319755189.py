from collections import deque
A = deque()
ans = []


def push(d, x):
    global A
    if d == 0:
        A.appendleft(x)
    elif d == 1:
        A.append(x)


def randomAccess(p):
    global A, ans
    if A != []:
        ans.append(A[p])
    else:
        print('RandomAccessError')


def pop(d):
    global A
    if d == 0:
        A.popleft()
    elif d == 1:
        A.pop()


def main():
    q = input()

    for i in range(int(q)):
        command = input().split()
        if len(command) == 3:
            query, operation, number = (int(x) for x in command)
            push(operation, number)
        else:
            query, number = (int(x) for x in command)
            if query == 1:
                randomAccess(number)
            else:
                pop(number)

    for i in range(len(ans)):
        print(ans[i])


if __name__ == "__main__":
    main()

