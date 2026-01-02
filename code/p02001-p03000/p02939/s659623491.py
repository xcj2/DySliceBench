import sys
def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def s(): return(input())

def main():
  S = s()
  cur = [[1,S[0],""],[0,"",S[0]]]
  nxt = []
  N = len(S)
  
  for i in range(1,N):
    for c,p,n in cur:
      if len(n)==1 and p!=n+S[i]:
        nxt.append([c+1,n+S[i],""])
      elif len(n)==0:
        nxt.append([c,p,n+S[i]])
        if p!=n+S[i]:
          nxt.append([c+1,n+S[i],""])
    nxt.sort(key = lambda x: x[0], reverse = True)
    nxt.sort(key = lambda x:(x[1],x[2]))
    cur = [nxt[0]]
    for j in range(1,len(nxt)):
      if cur[-1][1:] != nxt[j][1:]:
        cur.append(nxt[j])
    nxt = []
  r = -1
  for c,p,n in cur:
    if n == "":
      r = max(r,c)
  return r

if __name__ == "__main__":
  print(main())

      
