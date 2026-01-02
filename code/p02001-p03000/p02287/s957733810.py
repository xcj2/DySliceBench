def parent(i):
    return i//2
    
def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1
 
if __name__ == '__main__':
    n = int(input().rstrip())
    a = [-1]
    a += [int(i) for i in input().rstrip().split(" ")]
    for i in range(1, n+1):
        print("node {}: ".format(i), end = "")
        print("key = {}, ".format(a[i]),end = "") 
        if parent(i) >= 1:
            print("parent key = {}, ".format(a[parent(i)]), end = "")
        if left(i) <= n:
            print("left key = {}, ".format(a[left(i)]), end = "")
        if right(i) <= n:
            print("right key = {}, ".format(a[right(i)]), end = "")
        print()