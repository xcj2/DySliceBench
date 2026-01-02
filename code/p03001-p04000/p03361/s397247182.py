def myAnswer(H:int,W:int,S:list) -> int:
   for h in range(H):
      for w in range(W):
         target = S[h][w]
         if(target == "#"):
            if(h != 0 and S[h-1][w] == "#"):# 上を探索
               continue
            elif(w != 0 and S[h][w - 1] == "#"):# 右を探索
               continue
            elif(h != H-1 and S[h + 1][w] == "#"):# 下を探索
               continue
            elif(w != W -1 and S[h][w+1] == "#"):# 左を探索
               continue
            else:
               return "No"
   return "Yes"

def modelAnswer():
   return
def main():
   H,W = map(int,input().split())
   S = []
   for _ in range(H):
      S.append(list(input()))
   print(myAnswer(H,W,S[:]))
if __name__ == '__main__':
   main()