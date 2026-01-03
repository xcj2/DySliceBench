def myAnswer(H:int,W:int,A:list) -> str:
   counter = 0
   for a in A:
      counter += a.count("#")
   return "Possible" if(counter == H + W - 1) else "Impossible"

   # i = 0
   # j = 0
   # if(A[i][j] == "." or A[H-1][W -1] == "."):return "Impossible"
   # while True:
   #    print(i,j)
   #    if(i == H -1 and j == W - 1):
   #       return "Possible"
   #    else:
   #       tmp = []
   #       if(j != W - 1 and A[i][j + 1] == "#"):
   #          tmp.append([i,j + 1])
   #       if(i != H - 1 and A[i + 1][j] == "#"):
   #          tmp.append([i + 1,j])
   #       if(len(tmp) == 1):
   #          i,j = tmp[0][0],tmp[0][1]
   #       else:
   #          return "Impossible"


def modelAnswer():
   return
def main():
   H,W = map(int,input().split())
   A = []
   for _ in range(H):
      A.append(list(input()))
   print(myAnswer(H,W,A))
if __name__ == '__main__':
   main()