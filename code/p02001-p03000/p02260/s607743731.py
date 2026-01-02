def print_format(N,input_list,count):
    for i in range(N):
        if i != N-1:
            print(input_list[i],end=" ")
        else:
            print(input_list[i])
    print(count)

def selection_sort(N,input_list):
    swap_count = 0
    for i in range(N):
        minj = i
        for j in range(i,N):
            if input_list[j] < input_list[minj]:
                minj = j
        if i != minj:
            swap_count += 1
        input_list[i],input_list[minj] = input_list[minj],input_list[i]
    return input_list,swap_count

def main():
    N = int(input())
    input_list = [int(i) for i in input().split()]
    input_list,count = selection_sort(N,input_list)
    print_format(N,input_list,count)

if __name__ == "__main__":
    main()
