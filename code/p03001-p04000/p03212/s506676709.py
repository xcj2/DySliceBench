def main():
  n=[int(i) for i in list(input())]
  l=len(n)
  
  def abc_num(n,a,b,c):
    dp=[[0]*2 for i in range(l+1)]
    dp[0][0]=1
    for i in range(l):
      if n[i]<a:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][1]*3
      elif n[i]==a:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][1]*3
      elif n[i]<b:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][0]+dp[i][1]*3
      elif n[i]==b:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][0]+dp[i][1]*3
      elif n[i]<c:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][0]*2+dp[i][1]*3
      elif n[i]==c:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][0]*2+dp[i][1]*3
      else:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][0]*3+dp[i][1]*3
    return sum(dp[-1])
    
        
  def ab_num(n,a,b):
    dp=[[0]*2 for i in range(l+1)]
    dp[0][0]=1
    for i in range(l):
      if n[i]<a:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][1]*2
      elif n[i]==a:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][1]*2
      elif n[i]<b:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][0]+dp[i][1]*2
      elif n[i]==b:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][0]+dp[i][1]*2
      else:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][0]*2+dp[i][1]*2
    return sum(dp[-1])
  
  def a_num(x):
    x=int(''.join([str(i) for i in x]))
    three=int(''.join(['3']*l))
    five=int(''.join(['5']*l))
    seven=int(''.join(['7']*l))
    if x<three:
      return 0
    elif three<=x<five:
      return 1
    elif five<=x<seven:
      return 2
    else:
      return 3  

  ans=abc_num(n,3,5,7)
  ans-=(ab_num(n,3,5)+ab_num(n,3,7)+ab_num(n,5,7))
  ans+=a_num(n)
  for i in range(3,l):
    ans+=3**i-3*(2**i)+3
  print(ans)  
if __name__=='__main__':
  main()