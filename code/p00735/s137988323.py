def ms_number(n):
    count = 1
    msnumber_list = [6]
    while msnumber_list[-1] < n:
        msnumber_list.append(7 * count + 1)
        msnumber_list.append(7 * count + 6)
        count += 1

    return msnumber_list[:-1]


def ms_prime(n, msnumber_list):
    msprime_list = []
    msprime_flag = [0 for i in range(n + 1)]

    for i in msnumber_list:
        if msprime_flag[i] == 0:
            msprime_list.append(i)
            for j in msnumber_list:
                if i * j > n:
                    break
                msprime_flag[i * j] = 1

    return msprime_list


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


msnumber_list = ms_number(300000)
msprime_list = ms_prime(300000, msnumber_list)

answer = []
input_list = []

while True:
    n = int(input())
    if n == 1:
        break

    input_list.append(n)
    divisors = make_divisors(n)

    answer.append([d for d in divisors if d in msprime_list])


for i in range(len(input_list)):
    print(str(input_list[i]) + ": ", end="")
    print(*answer[i])
