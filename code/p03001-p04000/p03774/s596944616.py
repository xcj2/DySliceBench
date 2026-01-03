def myAnswer(N:int,M:int,A:list,B:list,C:list,D:list) ->int:
   for a,b in zip(A,B):
      ans = 10**10
      no = 0
      for n in range(M):
         c = C[n]
         d = D[n]
         distance = abs(a - c) + abs(b - d)
         if(ans > distance):
            ans = distance
            no = n+1
      print(no)


def modelAnswer():
   return
def main():
   N, M = map(int,input().split())
   A = []
   B = []
   C = []
   D = []
   for _ in range(N):
      a,b = map(int,input().split())
      A.append(a)
      B.append(b)
   for _ in range(M):
      c,d = map(int,input().split())
      C.append(c)
      D.append(d)
   myAnswer(N,M,A[:],B[:],C[:],D[:])

if __name__ == '__main__':
   main()