'''
5
H4 C9 S4 D2 C3
'''
N = int(input())
C1 = list(map(str, input().split()))
C2 = [None] * N

for i in range(N):
  C2[i] = C1[i]

def bubble(C, N):
  #count = 0
  for i in range(0, N-1, 1):
    for j in range(N-1, i, -1):
      #print("j:{} C[j-1]:{} C[j]:{}".format(j, C[j-1], C[j]))
      if (int(C[j-1][1]) > int(C[j][1])):
        C[j-1], C[j] = C[j], C[j-1]
        #count += 1
        #print("Swapped. C:{}".format(C))

  print(str(C).replace('[', '').replace(']', '').replace(',', '').replace('\'', ''))
  print("Stable") # because buddle sort is stable sort

def selection(C, N):
  for i in range(N):
    minj = i
    for j in range(i+1, N):
      if (int(C[minj][1]) > int(C[j][1])):
        minj = j
    C[minj], C[i] = C[i], C[minj]

  print(str(C).replace('[', '').replace(']', '').replace(',', '').replace('\'', ''))

def main():
  bubble(C1, N)
  selection(C2, N)

  if (C1 == C2):
    print("Stable")
  else:
    print("Not stable")

main()

