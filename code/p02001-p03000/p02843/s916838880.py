def myAnswer(X:int)-> int:
   # 100より下なら0
   if(X < 100) : return 0

   total = 0 #合計金額
   first = X % 10 #1桁目の数値
   secand = ((X // 10) % 10) *10 #2桁目の数値
   if(first <=5 and first >=1): # １桁目が0以上5以下なら1個で済む
      total += 100 + first
   elif(first >= 6):
      total += 200 + first #1桁目が6以上なら2個必要

   total += (secand//5)*105 # 2桁目は105円から作る
   # Xがtotal以上なら合計金額がちょうどになる。
   return 1 if(total <= X) else 0



def modelAnswer():
   tmp=1
def main():
   X = int(input())
   print(myAnswer(X))

if __name__ == '__main__':
   main()