'''
Accepted    　:No
difficult   　: 
ペナルティ　  　:5分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''

def myAnswer(N:int,K:int,A:list,B:list) -> int:
   dic = {}
   for a,b in zip(A,B):
      if a in dic.keys():
         dic[a] += b
      else:
         dic[a] = b
   total = 0
   for a,b in sorted(dic.items()):
      total += b
      if K <= total:
         return a

def modelAnswer():
   return
def main():
   N,K = map(int,input().split())
   A = []
   B = []
   for _ in range(N):
      a,b = map(int,input().split())
      A.append(a)
      B.append(b)
   print(myAnswer(N,K,A,B))
if __name__ == '__main__':
   main()