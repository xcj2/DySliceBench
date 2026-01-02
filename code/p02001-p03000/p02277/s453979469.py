def merge(A, left, mid , right):
  L = A[left:mid]
  R = A[mid:right]
  L.append(('J', 1000000001))
  R.append(('J', 1000000001))
  i = 0
  j = 0
  for k in range(left, right):
    if L[i][1] <= R[j][1]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1

def merge_sort(A, p ,r):
  if p + 1 < r:
    m = (p + r) // 2
    merge_sort(A, p, m)
    merge_sort(A, m, r)
    merge(A, p, m, r)

def partition(A, p, r): 
  x = A[r][1]
  i = p - 1
  for j in range(p, r):
    if A[j][1] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i + 1], A[r] = A[r], A[i + 1]
  return i + 1

def quick_sort(A, p, r):
  if p < r:
    q = partition(A, p, r)
    quick_sort(A, p, q - 1)
    quick_sort(A, q + 1, r)

n = int(input())

cards = []

for i in range(n):
  card, rank = input().split(" ")
  cards.append((card, int(rank)))
copy_cards = cards[:]

quick_sort(cards, 0, len(cards) - 1)
merge_sort(copy_cards, 0, len(cards))

stable = True
for x, y in zip(cards, copy_cards):
  if x != y:
    stable = False
    print('Not stable')
    break

if stable:
  print('Stable')

for card in cards:
  print("{} {}".format(card[0], card[1]))
