N = int(input())
A = [int(x) for x in input().split()]

def count(num, counter_list):
    if len(counter_list) == 0:
        counter_list.append([num, 0])
    current = counter_list[-1]     
    if current[0] == num:
        current[1] += 1
    else:
        counter_list.append([num, 1])

def calc(list):
    result = 0
    for item in list:
        cmp_count = item[1] - item[0]
        result += cmp_count if cmp_count >= 0 else item[1]
    return result

def main():
    A.sort()
    counter_list = []
    for i in range(N):
        count(A[i], counter_list)
    ans = calc(counter_list)
    print(ans)

if __name__ == '__main__':
    main()
