'''
ABC 131 D:Megalomania
Accepted    　:Yes
difficult   　: 
ペナルティ　  　:5分
実際の回答時間  :9分
WAの回数　     :0回
合計時間　　  　:9分
'''
import sys
input = sys.stdin.readline

def myAnswer(N:int,A:list,B:list) -> str:
   dic = {}
   # 締め切り時間をkey、作業時間をvalueにした辞書を作成
   for a,b in  zip(A,B):
      if(b in dic.keys()):
         dic[b].append(a)
      else:
         dic[b] = [a]
   now = 0
   dic = sorted(dic.items())
   for deadline,time in dic:
      time.sort()
      # print(deadline,time)
      for t in time:
         if(deadline < now + t):
            return "No"
         now += t
   return "Yes"

def modelAnswer(N:int,dic:dict) -> str:
   now = 0
   dic = sorted(dic.items())
   for deadline,time in dic:
      time.sort()
      for t in time:
         if(deadline < now + t):
            return "No"
         now += t
   return "Yes"

def main():
   N = int(input())
   dic = {}
   # A = []
   # B = []
   for _ in range(N):
      a,b = map(int,input().split())
      if(b in dic.keys()):
         dic[b].append(a)
      else:
         dic[b] = [a]
      # A.append(a)
      # B.append(b)
   print(modelAnswer(N,dic))
if __name__ == '__main__':
   main()