def print_format(N,input_list, count):
    for i in range(N):
        if i != N-1:
            print(input_list[i],end=" ")
        else :
            print(input_list[i])
    print(count)
def bubble_sort(N,input_list):
    count = 0
    flag = True
    while flag:
        flag = False
        for j in range(1,N)[::-1]:
            if input_list[j] < input_list[j-1]:
                input_list[j],input_list[j-1] = input_list[j-1],input_list[j]
                count += 1
                flag = True
    return input_list, count

def main():
    N = int(input())
    input_list = [int(i) for i in input().split()]
    input_list,count = bubble_sort(N,input_list)
    print_format(N,input_list,count)


if __name__ == "__main__":
    main()
