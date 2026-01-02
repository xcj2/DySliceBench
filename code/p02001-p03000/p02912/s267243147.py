n, m = map(int, input().split())
a = [int(i) for i in input().split()]

#%%

# n, m, a = 3, 3, [1,2,3,4,7,9, 10,8,16,14]

#%%
max_heap = [a[0]]
#%%
def add_heap(array, number):
    array.append(number)

    def swap(array, number, idx):
        if idx == 1:
            return array[idx-1]

        ai = array[idx-1]
        target_idx = (idx//2)
        target = array[target_idx-1]
        
        if ai >= target:
            array[idx-1], array[target_idx-1] =  target, ai

            number = swap(array, number, target_idx)
        else:
            return array[idx-1]

    return swap(array, number, len(array))


#%%
for ai in a[1:]:
    add_heap(max_heap, ai)

#%%
for _ in range(m):
    
    #half
    max_heap[0] //= 2
    
    def sort_heap(array, number, idx):
        top = number
        left_idx = idx*2
        right_idx = idx*2 + 1
        
        if left_idx > len(array):
            left = -1
        else:
            left = array[left_idx - 1]

        if right_idx > len(array):
            right = -1
        else:        
            right = array[right_idx - 1]

        if top >= left and top >= right:
            return array
        elif left > right:
            array[idx-1], array[left_idx-1] = left, top
            sort_heap(array, top, left_idx)
        else:
            array[idx-1], array[right_idx-1] = right, top
            sort_heap(array, top, right_idx)

    sort_heap(max_heap, max_heap[0], 1)

#%%
print(sum(max_heap))

#%%
