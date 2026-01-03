'''
Accepted    　:No
difficult   　: 
ペナルティ　  　:5分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''

def myAnswer(N:int,M:int,X:list,Y:list) -> int:
   ans = {0}
   box = [1] * N
   for x,y in zip(X,Y):
      if(x-1 in ans):
         if(box[x - 1]==1):
            ans.remove(x-1)
         ans.add(y-1)
      box[x-1] -= 1
      box[y-1] += 1
   return len(ans)

def modelAnswer():
   return
def main():
   N,M = map(int,input().split())
   X = []
   Y = []
   for _ in range(M):
      x,y=map(int,input().split())
      X.append(x)
      Y.append(y)
   print(myAnswer(N,M,X,Y))
if __name__ == '__main__':
   main()