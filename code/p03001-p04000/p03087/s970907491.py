'''
Accepted    　:No
difficult   　: 
ペナルティ　  　:5分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''

def myAnswer(N:int,Q:int,S:str,L:list,R:list) -> None:
   pre = S[0]
   accum = [0]
   for s in S[1:]:
      if(pre == "A" and s =="C"):
         accum.append(accum[-1] + 1)
      else:
         accum.append(accum[-1])
      pre = s
   for l,r in zip(L,R):
      print(accum[r-1] - accum[l-1])


def modelAnswer():
   return
def main():
   N,Q = map(int,input().split())
   S =input()
   L = []
   R = []
   for _ in range(Q):
      l,r = map(int,input().split())
      L.append(l)
      R.append(r)
   myAnswer(N,Q,S,L,R)


if __name__ == '__main__':
   main()