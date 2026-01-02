N = input()
K = int(input())

def K1(N):
  le = len(N)
  if le == 1:
    return int(N)
  else:
    return 9*(le-1)+int(N[0])
def K2(N):
  le = len(N)
  if le == 1:
    return 0
  else:
    j=1
    if int(N[j]) == 0 and j != le-1:
      while int(N[j]) == 0:
        j+=1
        if j == le-1:
          break
        
    n = N[j:le]
    return (9**2)*((le-1)*(le-2)//2) + K1(n) +(int(N[0])-1)*K1("9"*(le-1))
  
def K3(N):
  le = len(N)
  if le == 1 or le == 2:
    return 0
  else:
    j=1
    if int(N[j]) == 0 and j != le-1:
      while int(N[j]) == 0:
        j+=1
        if j == le-1:
          break
        
    n2 = N[j:le]
    
    return (9**3)*((le-1)*(le-2)*(le-3)//6) + K2(n2) + (int(N[0])-1)*K2("9"*(len(N)-1))
if K == 1:
  print(K1(N))
    
if K == 2:
  print(K2(N))
  
if K == 3:
  print(K3(N))
  