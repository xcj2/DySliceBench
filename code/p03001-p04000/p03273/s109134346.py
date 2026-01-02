import sys

def del_add_dot_list(a):
    del_index = []
    for i in range(len(a)):
        if all(map(lambda x: x=='.', a[i])):
            del_index.append(i)
    for i in del_index[::-1]:
        del a[i]
    return a

def spin(a):
    if len(a[0]) == 1:
        return [''.join(list(map(lambda x: x[0], a)))]
    else:
        return [''.join(list(map(lambda x: x[0], a)))] + spin(list(map(lambda x: x[1:], a)))

def main():
    sys.setrecursionlimit(10000)
    h, w = map(int, input().split())
    a = [input() for i in range(h)]
    deleted = spin(del_add_dot_list(spin(del_add_dot_list(a))))
    [print(l) for l in deleted]

if __name__ == '__main__':
    main()