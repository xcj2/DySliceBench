class Counting_Sort():
    def __init__(self, N, input_number_list):
        self.N = N
        self.number_list = input_number_list
        self.print_number_list = list()

    def counting_sort(self):
        counting_list = list()
        for i in range(10001):
            counting_list.append(0)
        for i in range(self.N):
            counting_list[self.number_list[i]] += 1
            self.print_number_list.append(0)
        for i in range(1,10001):
            counting_list[i] += counting_list[i-1]
        for i in range(self.N-1,-1,-1):
            self.print_number_list[counting_list[self.number_list[i]]-1] = self.number_list[i]
            counting_list[self.number_list[i]] -= 1

def print_number_list(number_list, N):
    for i in range(N):
        if i != N - 1:
            print(number_list[i],end=' ')
        else:
            print(number_list[i])

def main():
    N = int(input())
    input_number_list = [int(i) for i in input().split()]
    sort = Counting_Sort(N,input_number_list)
    sort.counting_sort()
    print_number_list(sort.print_number_list,N)

if __name__ == "__main__":
    main()
