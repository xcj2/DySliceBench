
ans = 0

def main():
    n = int(input())
    lst = list(map(int,input().split()))

    all_lst=[lst]
    make_lst(all_lst)
    print(ans)


def minus(lst):
    m = min(lst)
    global ans
    ans+=m
    return list(map(lambda x: x-m, lst))

def make_lst(all_lst):
    #tmp =0

    for lst in all_lst:
        #tmp +=1
        #if tmp >= 20:
        #    print(all_lst)
        #    exit()

        if lst != []:
            lst = minus(lst)
        lst = " ".join(map(str,lst)).split(" 0")
        for i in lst:
            if i.split() != []:
                sp_list = list(map(int,i.split()))
                if 0 in sp_list:
                    sp_list.remove(0)

                all_lst.append(sp_list)


if __name__ == "__main__":
        main()
