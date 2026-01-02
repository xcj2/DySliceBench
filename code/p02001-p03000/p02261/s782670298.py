def bubble_sort(N ,num1, suit1): # バブルソート(常に安定)
   # print('\nnum1 & suit1 adress')
   # print(id(num1), id(suit1))
   for i in range(N): # 未ソート部分列は一つずつ減っていく
      for j in range(N-1, i, -1): # 一番後ろ(配列的にはN-1番目)から未ソート部分列の先頭(i+1)まで
         if num1[j] < num1[j-1]: # 後ろより前の方が大きかったら交換
            num1[j], num1[j-1] = num1[j-1], num1[j]
            suit1[j], suit1[j-1] = suit1[j-1], suit1[j]
   return join_trump(N, num1, suit1)

def selection_sort(N, num2, suit2): # 選択ソート(常に安定ではない)
   for i in range(N):
      minj = i # とりあえず未ソート部分列の先頭A[i]を一番小さいことにしておく(indexを記憶)
      for j in range(i+1, N): # 未ソート部分列の次から最後まで，より小さいものを探す
         if num2[j] < num2[minj]: # もし小さいのがあれば
            minj = j # 最小値のindexを変更
      if num2[minj] < num2[i]: # 未ソート部分列中の最小値と未ソート部分列の先頭を比較
         num2[i], num2[minj] = num2[minj], num2[i] # 先頭の方が大きければ入れ替える
         suit2[i], suit2[minj] = suit2[minj], suit2[i]
   return join_trump(N, num2, suit2)

def join_trump(N, num3, suit3):
   trump = [''] * N
   for i in range(N):
      trump[i] = suit3[i] + str(num3[i])
   return trump

# Selection Sortが安定かどうかを調べる
def is_stable(x, y, N): # x: bubble_ans, y: selec_ans
   for i in range(N):
      if x[i]!=y[i]:
         print('Not stable')
         return 0
   print('Stable')

N = int(input()) # カード枚数の入力
# card = list(map(int, input().split())) # 「1 2 3…」のような配列入力
trump = input().split() # 今回は文字列入力なのでこれだけでよい
suit1 = [''] * N # トランプの絵札だけ用配列
num1 = [0] * N   # トランプの数字だけ用配列
for i in range(N):           # トランプの絵札を数字を別々にする
   suit1[i] = trump[i][0]     # 絵札だけ
   num1[i] = int(trump[i][1]) # 数字だけ
suit2, num2 = suit1[:], num1[:]
# print('\nnum & suit adress')
# print(id(num1), id(suit1))
# print(id(num2), id(suit2))

# # Bubble Sortによる出力(常に安定)
bubble_ans = bubble_sort(N, num1, suit1)
print(*bubble_ans)
print('Stable')

# # Selection Sortによる出力(安定とは限らない)
selec_ans = selection_sort(N, num2, suit2)
print(*selec_ans)
is_stable(bubble_ans, selec_ans, N)
