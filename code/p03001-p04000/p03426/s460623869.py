def get_next_int():
    return int(float(input()))
def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])

def main():
    h, w, d = get_next_ints()
    values = {}
    for i in range(h):
        line_data = get_next_ints()
        for j, a in enumerate(line_data):
            values[a] = (i, j)
    from collections import defaultdict
    distances = defaultdict(int)
    
    for a in range(1,h * w + 1):
        i, j = values[a]
        prev = a - d
        if prev in values:
            prev_i, prev_j = values[prev]
            distances[a] = abs(prev_i - i) + abs(prev_j - j) + distances[prev]
        else:
            distances[a] = 0
    q = get_next_int()
    for k in range(q):
        r, l = get_next_ints()
        print(distances[l] - distances[r] )
        
if __name__ == '__main__':
    main()