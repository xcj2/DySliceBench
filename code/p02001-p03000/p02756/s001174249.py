from collections import deque
def myAnswer(S:deque,Q:int,querys:list) -> str:
   setF = {1,2}
   reverse = False
   for query in querys:
      command = int(query[0])
      if(command == 1):
         reverse = not reverse
      else:
         F = int(query[1])
         C = query[2]
         if(reverse):
            F = set(setF - {F}).pop()
         S.appendleft(C) if(F == 1) else S.append(C)

   if(reverse):S.reverse()
   return "".join(S)

def modelAnswer():
   return
def main():
   S = deque(input())
   Q = int(input())
   querys = [list(map(str,input().split())) for _ in range(Q)]
   print(myAnswer(S,Q,querys))



if __name__ == '__main__':
   main()