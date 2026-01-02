As = [list(map(int, input().split())) for x in range(3)]
N = int(input())
bs = [int(input()) for x in range(N)]


def create_bingo_card():
  result = [[0, 0, 0] for x in range(3)]
  i = 0
  while True:
    i2 = 0
    while True:
      if bs[i2] in As[i]:
        result[i][As[i].index(bs[i2])] += 1
      i2 += 1
      if i2 == len(bs):
        break
    i += 1
    if i == len(As):
      break
  return result


def solvd(bingo):
  tmp = [bingo[0][0], bingo[1][1], bingo[2][2]]
  if check1(tmp):
    print("Yes")
    return

  tmp = [bingo[0][2], bingo[1][1], bingo[2][0]]
  if check1(tmp):
    print("Yes")
    return

  r = 0
  for x in range(3):
    tmp = [bingo[0][x], bingo[1][x], bingo[2][x]]
    if check1(tmp):
      print("Yes")
      return

    bingoSet = set(bingo[x])
    if check2(bingoSet):
      r += 1

  if r >= 1:
    print("Yes")
    return
  print("No")


def check1(s):
  return s.count(1) == 3


def check2(s):
  return not (0 in list(s))


def main():
  Cs = create_bingo_card()
  solvd(Cs)


if __name__ == "__main__":
    main()