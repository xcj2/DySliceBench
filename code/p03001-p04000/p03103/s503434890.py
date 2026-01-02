import sys

class Shop:
  def __init__(self, A, B):
    self.price = A
    self.limit = B

def merge(a, b):
    """ Merge of two sorted arrays (iterative version)
    
    IN:  sorted arrays a and b
    OUT: merging of a and b into one sorted array
    """
    if not a or not b or a[-1].price < b[0].price:
        return a + b
    res = [ a[0] for i in range(len(a)+len(b)) ]
    next_a = 0
    last_a = len(a)-1
    last_b = len(b)-1
    for i in range(len(res)):
        next_b = i - next_a
        if (next_a > last_a) or ((next_b <= last_b) and (a[next_a].price > b[next_b].price)):
            res[i] = b[next_b]
        else:
            res[i] = a[next_a]
            next_a += 1
    return res


def mergeSort(array):
    """ Sorting function (merge sort)
    IN: arbitrary array
    OUT: sorted array
    """

    # replace the lines below with your own code (minimum requirement for project 2)
    unit_length = 2
    array = [[i] for i in array]
    while len(array) != 1:
        temp = []
        len_arr = len(array)
        for i in range(0, len_arr, unit_length):
            if i == len_arr - 1:
                temp.append(array[i])
            else:
                temp.append(merge(array[i], array[i+1]))
        array = temp
    return array[0]
  

a = list(map(int, input().split()))

shop = a[0]
drink = a[1]

shops = []
for i in range(shop):
  a = list(map(int, input().split()))
  shops.append(Shop(a[0], a[1]))

shops = mergeSort(shops)

ans = 0
tmp = 0
for i in shops:
  B = i.limit
  if B > drink:
    tmp = drink
    drink = 0
  else:
    tmp = B
    drink -= B
  
  ans += i.price * tmp
  if drink == 0:
    break

print(ans)
