from collections import deque

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    B = [0] * n
    # ansList = []
    ansList = deque()

    def makeList(num):
        start = num + 1
        mul = n // start
        return [start * j - 1 for j in range(1, mul+1)]


    def makeRes(indices):
        flag = 0
        for elm in indices:
            if B[elm] == 1:
                flag = (flag + 1) % 2
        return flag


    for i in range(n-1, -1, -1):
        if i + 1 >  n / 2:
            if A[i] == 1:
                B[i] = 1
                ans += 1
                ansList.appendleft(i+1)
        else:
            indices = makeList(i)
            # print(indices)
            res = makeRes(indices)
            # print(res)
            if A[i] != res:
                B[i] = 1
                ans += 1
                ansList.appendleft(i+1)

    print(ans)

    if ans != 0:
        print(*(list(ansList)))


if __name__ == "__main__":
    main()