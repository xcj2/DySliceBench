import sys
print = sys.stdout.write

def insert(key, queue):
    """priority queueに値を代入する.
    
    Args:
        key (int): priority queueに代入する数値.

    Notes:
        indexは扱いやすさのため1~nを想定してしている.
        配列値取得時にはpythonの仕様に合わせて-1としている.
    """
    queue.append(key)
    index = n
    if index == 1:
        return
    parent_index = index//2
    while parent_index and queue[parent_index-1] < key:
        queue[index-1] = queue[parent_index-1]
        index, parent_index = parent_index, parent_index//2
    queue[index-1] = key
    
def extract_max(queue):
    index = 1
    root = queue[0]
    l_index = index*2
    num = n
    while l_index < num:
        ql, qr = queue[l_index-1], queue[l_index]
        bigger = (l_index, ql) if ql > qr else (l_index+1, qr)
        if bigger[1] > root:
            next_index = bigger[0]
            queue[index-1] = queue[next_index-1]
            index = next_index
            l_index = index*2
        else:
            break
        
    if l_index == num:
        if queue[l_index-1] > root:
            queue[index-1] = queue[l_index-1]
            index = l_index
    queue[index-1] = root


def main():
    S = []
    global n
    n = 0
    for operation in sys.stdin.readlines():
        if operation[0] == "i":
            n += 1
            insert(int(operation[7:]), S)
        elif operation[1] == "x":
            print("{}\n".format(S[0]))
            S[0] = S.pop()
            n -= 1
            extract_max(S)
        elif operation == "end":
            break

if __name__ == "__main__":
    main()
