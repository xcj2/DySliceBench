import itertools
import math
def myAnswer(N:int,D:int,X:list)->int:
   l = [i for i in range(N)]
   total = 0
   for i in itertools.combinations(l,2):
      distance = 0
      for n in range(D):
         distance += (X[i[0]][n] - X[i[1]][n])**2
      distance = distance**0.5
      if(distance == math.ceil(distance)):
         total += 1
   return total

   

def modelAnswer():
   tmp=1
def main():
   N,D = map(int,input().split())
   X = []
   for _ in range(N):
      X.append(list(map(int,input().split())))
   print(myAnswer(N,D,X[:]))

if __name__ == '__main__':
   main()