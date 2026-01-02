
def B():
    def odd(x):
        return int(3 * x + 1)
    
    def even(x):
        return int(x / 2)

    def is_unique(seq):
        return len(seq) == len(set(seq))

    s = int(input())

    a_list = []
    a_list.append(s)
    
    for i in range(1000000):
        ai = a_list[i]

        if ai % 2 == 0:
            a_list.append(even(ai))
        else:
            a_list.append(odd(ai))

        if is_unique(a_list) is not  True:
            # (i + 1) + 1
            print(i + 1 + 1)
            break
    

if __name__== '__main__':
    B()
