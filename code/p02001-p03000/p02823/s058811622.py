# coding: utf-8

def pattern1(N, A, B):
  left = B - 1
  right= N - A
  if left < right:
    return left
  else:
    return right  
      
def pattern2(N, A, B):
  round_elapsed_mid = (A - 1) + 1
  B_position = B - round_elapsed_mid
  offset = B_position - 1
  if offset % 2 == 0:
    return (offset // 2 + round_elapsed_mid)
  
def pattern3(N, A, B):
  round_elapsed_mid = (N - B) + 1
  A_position = A + round_elapsed_mid
  offset = N - A_position
  if offset % 2 == 0:
    return (offset // 2 + round_elapsed_mid)

N, A, B = (int(n) for n in input().split())
offset = B - A
if offset % 2 == 0:
  print(offset // 2)
else:
  candi1 = pattern1(N, A, B)
  candi2 = pattern2(N, A, B)
  candi3 = pattern3(N, A, B)
  print(min([candi1, candi2, candi3]))
  