def fun_replace(str1,str2,a,b):
    str1_list = list(str1)
    str2_list = list(str2)
    for i in range(b-a+1):
        str1_list[a+i]=str2_list[i]
    str1_changed = "".join(str1_list)
    return str1_changed

def fun_reverse(str1,a,b):
    tmp_str_list=list(str1[a:b+1])
    tmp_str_list.reverse()
    str1_list = list(str1)
    for i in range(b-a+1):
        str1_list[a+i] = tmp_str_list[i]
    str1_changed = "".join(str1_list)
    return str1_changed

def fun_print(str1,a,b):
    for i in range(a,b+1):
        print("%s"%(str1[i]),end="")
    print()


T = str(input())
change_num=int(input())
for order_num in range(change_num):
    order=input().split()

    if str(order[0]) == 'replace':
        T=fun_replace(T,str(order[3]),int(order[1]),int(order[2]))
    elif str(order[0]) == 'reverse':
        T=fun_reverse(T,int(order[1]),int(order[2]))
    else:
        fun_print(T,int(order[1]),int(order[2]))

