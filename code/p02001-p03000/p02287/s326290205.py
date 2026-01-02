import sys

def parent(i):
    return i // 2
def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1

# sys.stdin = open('input.txt')

size = int(input())
heap = [i for i in map(int, input().split())]
heap = [0] + heap # 1 origin

for i in range(1, size+1):
    print('node ' + str(i) + ': key = ' + str(heap[i]) + ', ', end='')
    if parent(i) >= 1:
        print('parent key = ' + str(heap[parent(i)]) + ', ', end='')
    if left(i) <= size:
        print('left key = ' + str(heap[left(i)]) + ', ', end='')
    if right(i) <= size:
        print('right key = ' + str(heap[right(i)]) + ', ', end='')
    print('')

