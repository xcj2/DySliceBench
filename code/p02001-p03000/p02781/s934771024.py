#https://atcoder.jp/contests/abc154/tasks/abc154_e

def oneNum(N):
    answer = 0

    while(N > 0):
        if(N >= 9):
            answer = answer + 9
        else:
            answer = answer + N
        
        N = N // 10

    return answer

def twoNum(N):
    answer = 0

    strN = str(N)
    topN = int(strN[0])
    lenN = len(strN)

    if(lenN != 1):
        answer = answer + oneNum(int(strN[1:])) + (topN - 1) * oneNum(int('9' * (lenN - 1)))
        N = int('9' * (lenN - 1))

    while(N >= 10):
        N = N // 10
        answer = answer + 9 * oneNum(N)

    return answer

def main():
    N = int(input())
    K = int(input())

    answer = 0

    if(K == 1):
        answer = oneNum(N)

    elif(K == 2):
        answer = twoNum(N)

    else:
        strN = str(N)
        topN = int(strN[0])
        lenN = len(strN)

        answer = answer + twoNum(int(strN[1:])) + (topN - 1) * twoNum(int('9' * (lenN - 1)))

        N = int('9' * (lenN - 1))

        while(N >= 100):
            N = N // 10
            answer = answer + 9 * twoNum(N)

    print(answer)

if __name__ == "__main__":
    main()