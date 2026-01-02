n = int(input())

def parent(i):
    i += 1
    return int(i/2) -1

def left(i):
    i += 1
    return 2*i -1

def right(i):
    i += 1
    return 2*i + 1 -1

A = [int(i) for i in input().split()]

print('node {}: key = {}, left key = {}, right key = {}, '.format(1, A[0], A[left(0)], A[right(0)]))

for i in range(1, len(A)):
    output = 'node {}: key = {}, parent key = {}, '.format(i+1, A[i], A[parent(i)])
    left_i = left(i)
    if(left_i < len(A)):
        output += 'left key = {}, '.format(A[left_i])
    right_i = right(i)
    if(right(i) < len(A)):
        output += 'right key = {}, '.format(A[right_i])
        
    print(output)
    
