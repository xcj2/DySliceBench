A = []
ans = []


def pushBack(x):
    A.append(x)


def randomAccess(p):
    if A != []:
        ans.append(A[p])
    else:
        print('RandAccError')


def popBack():
    if A != []:
        del A[-1]
    else:
        print('DelError')


def main():
    q = input()
    for i in range(int(q)):
        try:
            query, number = (int(x) for x in input().split())
        except ValueError:
            popBack()
            continue

        if query == 0:
            pushBack(number)
        elif query == 1:
            randomAccess(number)

    for i in range(len(ans)):
        print(ans[i])


if __name__ == "__main__":
    main()

