STABLE = 'Stable'
UNSTABLE = 'Not stable'


def main():
  card_num = int(input())
  cards = input().split()

  bubble_sorted = bubble_sort(cards, card_num)
  select_sorted = select_sort(cards, card_num)

  stability = True
  for i, c in enumerate(select_sorted):
    if c != bubble_sorted[i]:
      stability = False
      break
  stability = STABLE if stability else UNSTABLE

  print(' '.join(bubble_sorted))
  print(STABLE)

  print(' '.join(select_sorted))
  print(stability)

  return 0


def order(card_sym):
  order = int(card_sym[1])
  return order


def select_sort(elements, element_num):
  elements = list(elements)

  for i in range(0, element_num - 1):
    min_val = order(elements[i + 1])
    min_index = i + 1
    for j in range(i + 1, element_num):
      if order(elements[j]) < min_val:
        min_val = order(elements[j])
        min_index = j
    if order(elements[i]) > order(elements[min_index]):
      elements[i], elements[min_index] = elements[min_index], elements[i]

  return elements


def bubble_sort(elements, element_num):
  elements = list(elements)

  for i in range(1, element_num):
    for j in reversed(range(i, element_num)):
      if order(elements[j - 1]) > order(elements[j]):
        elements[j - 1], elements[j] = elements[j], elements[j - 1]

  return elements


if __name__ == '__main__':
  main()