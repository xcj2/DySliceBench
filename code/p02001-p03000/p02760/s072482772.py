class BingoCard():
  A1 = []
  A2 = []
  A3 = []
  
  def __init__(self):
    self.A1 = [int(x) for x in input().split(' ')]
    self.A2 = [int(x) for x in input().split(' ')]
    self.A3 = [int(x) for x in input().split(' ')]

  def BingoProgress(self):
    N  = int(input())
    for i in range(N):
      B = int(input())
      if B in self.A1:
        self.A1[self.A1.index(B)] = 0
      if B in self.A2:
        self.A2[self.A2.index(B)] = 0
      if B in self.A3:
        self.A3[self.A3.index(B)] = 0

  def BingoJudge(self):
    flg = 0
    #横判定
    if sum(self.A1) == 0 or sum(self.A2) == 0 or sum(self.A3) == 0:
      flg = 1
    
    #縦判定
    if flg == 0:
      for i in range(3):
        if (self.A1[i] + self.A2[i] + self.A3[i]) == 0:
          flg = 1
          break
          
    #斜め判定
    if flg == 0:
      if (self.A1[0] + self.A2[1] + self.A3[2]) == 0 or (self.A1[2] + self.A2[1] + self.A3[0]) == 0:
        flg = 1

    #ビンゴ判定
    print('Yes' if flg == 1 else 'No')
    
def main():
  Bingo = BingoCard()
  Bingo.BingoProgress()
  Bingo.BingoJudge()

if __name__=='__main__':
  main()