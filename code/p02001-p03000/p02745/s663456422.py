def main():
  a = input()
  b = input()
  c = input()
  ab = [None]*20000
  ac = [None]*20000
  bc = [None]*20000
  def match(c1,c2):
    return (c1=='?')or(c2=='?')or(c1==c2)

  A = len(a)
  B = len(b)
  C = len(c)
  def solve(d1,d2,n,m,l):
    for i in range(n):
      for j in range(m):
        if not(match(d1[i],d2[j])):
          l[i-j+10000]=True
    return l
  ab = solve(a,b,A,B,ab)
  ac = solve(a,c,A,C,ac)
  bc = solve(b,c,B,C,bc)
  ans = 6000
  AB = A+B
  AC = A+C
  for i in range(-AC,AC,1):
    for j in range(-AB,AB,1):
      if (not(ab[i+10000]))and(not(ac[j+10000]))and(not(bc[j-i+10000])):
        L = min(0,min(i,j))
        R = max(A,max(B+i,C+j))
        ans = min(ans,R-L)
  print(ans)
  
main()