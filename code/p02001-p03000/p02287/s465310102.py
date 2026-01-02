import sys

def parent(i):
    return int(i/2)

def left(i):
    return 2 * i

def right(i):
    return (2 * i) + 1

if __name__ == "__main__":
    n = int(input())
    node = [None]
    node.extend(list(map(int, input().split())))
    for i in range(1,n+1):
        sys.stdout.write("node {}: key = {}, ".format(i, node[i])) 
        p = parent(i)
        if 0 < p <= n:
            sys.stdout.write("parent key = " + str(node[p]) + ", ")
        l = left(i)
        if 0 < l <= n:
            sys.stdout.write("left key = " + str(node[l]) + ", ")
        r = right(i)
        if 0 < r <= n:
            sys.stdout.write("right key = " + str(node[r]) + ", ")
        sys.stdout.write("\n")

