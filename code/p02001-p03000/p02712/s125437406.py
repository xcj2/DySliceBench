a=int(input())

def sum30():
  return (1+2+4+7+8+11+13+14+16+17+19+22+23+26+28+29)

def sumx(x):
  ret = 0
  if(x ==0):
    return ret
  
  for j in range(1,x+1):
    if(j%3 != 0 and j%5 != 0):
      ret+=j
  return ret

def numx(x):
  ret = 0
  if(x ==0):
    return ret
  
  for j in range(1,x+1):
    if(j%3 != 0 and j%5 != 0):
      ret+=1
  return ret
sum=0

i=1
#if()
#sum+=temp*sum30()+sumx(a%30)
while(a > 0):
  if(a >= 30):
    temp=(i-1)*30*16+sum30()
    #print(temp)
    sum+=temp
  else:
    sum+=(i-1)*30*numx(a)+sumx(a)
  i+=1
  a-=30
#while(temp > 0):
#  sum+= temp*sum30()
#  temp-=1

    
print(sum)
