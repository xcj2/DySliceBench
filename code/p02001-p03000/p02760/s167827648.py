
def myAnswer(A:list,B:list,N:int) -> str:
   bingo=[[0,0,0] for i in range(3)]
   for b in B:
      for i,a in enumerate(A):
         if(b in a):
            bingo[i][a.index(b)] = 1
            break
   tate=[0,0,0]
   for n,b in enumerate(bingo):
      if(sum(b) == 3):
         return "Yes"
      for i in range(3):
         tate[i] += b[i]
   if(3 in tate): return "Yes"
   if(bingo[1][1] == 1):
      if((bingo[0][0] == 1 and bingo[2][2] == 1) or (bingo[0][2]==1 and bingo[2][0]==1)):
         return "Yes"
   return "No"

def modelAnswer():
   tmp=1
def main():
   A=[]
   B=[]
   for _ in range(3):
      A.append(list(map(int,input().split())))
   N = int(input())
   for _ in range(N):
      B.append(int(input()))
   print(myAnswer(A[:],B[:],N))

if __name__ == '__main__':
   main()