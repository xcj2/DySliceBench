N, Q = map(int, input().split())
s = input()
t_list, d_list = list(), list()
for i in range(Q):
    t, d = input().split()
    t_list.append(t)
    d_list.append(d)


def go_away_to_left(idx):
    for t, d in zip(t_list, d_list):
        if s[idx] == t:
            if d == 'L':
                idx = idx - 1
            else:
                idx = idx + 1
        
        if idx == -1:
            return True
        
        elif idx == N:
            return False
    
    return False


def go_away_to_right(idx):
    for t, d in zip(t_list, d_list):
        if s[idx] == t:
            if d == 'L':
                idx = idx - 1
            else:
                idx = idx + 1
        
        if idx == N:
            return True
        
        elif idx == -1:
            return False
    
    return False


def binary_search_left(boundary, pyfunc):
    """search left boundary index where pyfunc returns True
    Args:
        boundary (tuple): [a, b)
        pyfunc
    Returns:
        index (int)
    """
    idx = sum(boundary) // 2
    if pyfunc(idx):
        boundary = (idx, boundary[1])
    else:
        boundary = (boundary[0], idx)
    
    if (boundary[1] - boundary[0]) == 1:
        return boundary[0]
    else:
        return binary_search_left(boundary, pyfunc)


def binary_search_right(boundary, pyfunc):
    """search right boundary index where pyfunc returns True
    Args:
        boundary (tuple): (a, b]
        pyfunc
    Returns:
        index (int)
    """
    idx = sum(boundary) // 2
    if pyfunc(idx):
        boundary = (boundary[0], idx)
    else:
        boundary = (idx, boundary[1])
    
    if (boundary[1] - boundary[0]) == 1:
        return boundary[1]
    else:
        return binary_search_right(boundary, pyfunc)

left = binary_search_left((-1, N), go_away_to_left)
right = binary_search_right((-1, N), go_away_to_right)
if left >= right:
    print(0)
else:
    print(right - left - 1)
# if left >= right:
#     golem_del = N
# else:
#     golem_del = (left - -1) + (N - right)
# print(N - golem_del)
