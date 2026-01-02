#■標準入力ショートカット

def get_next_int():
    return int(float(input()))
def get_next_str():
    return input()

def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])
def get_next_strs(delim=" "):
    return tuple(input().split(delim))

def get_next_by_types(*value_types,delim=" "):
    return tuple([t(x) for t, x in zip(value_types,input().split(delim))])

def main():
    n = get_next_int()
    from collections import defaultdict
    data = defaultdict(int)
    
    for i in range(2):
        for j, value in enumerate(get_next_ints()):
            data[(i,j)] = value
    
    max_get = defaultdict(int)
    
    for i in range(2):
        for j in range(n):
            max_get[(i,j)] = data[(i,j)] + max(max_get[(i-1,j)],max_get[(i,j-1)])
    
    return max_get[(1,n-1)]


if __name__ == '__main__':
    print(main())
    