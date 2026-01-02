def myAnswer(A: list, B: list, N: int) -> str:
    clomn = [0, 0, 0]
    bingoCard = [[0, 0, 0] for i in range(3)]
    row = [0, 0, 0]
    # マスが空くがどうかの判定
    for b in B:
        for i, a in enumerate(A):
            if(b in a):
                bingoCard[i][a.index(b)] = 1
                clomn[i] += 1
                row[a.index(b)] += 1
                break
   #  for n, b in enumerate(bingoCard):
   #      if(sum(b) == 3):
   #          return "Yes"  # 横の判定

    # 縦の判定(列ごとの合計が3である列があったかどうか)
    if(3 in row or 3 in clomn):
        return "Yes"

    # 斜めの判定
    if(bingoCard[1][1]):
        if((bingoCard[0][0] and bingoCard[2][2]) or (bingoCard[0][2] and bingoCard[2][0])):
            return "Yes"

    # 縦、横、斜めに当てはまらなければ,No
    return "No"


def modelAnswer():
    tmp = 1


def main():
    A = []
    B = []
    for _ in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    for _ in range(N):
        B.append(int(input()))
    print(myAnswer(A[:], B[:], N))


if __name__ == '__main__':
    main()
