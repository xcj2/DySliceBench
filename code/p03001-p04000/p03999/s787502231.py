def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

S = one_str()

num_list = list(S)

start_bit=2**(len(S)-1)
end_bit = 2**(len(S))

def get_sums(array, bit):
    sums = 0
    start = 0
    end = 0
    for i,s in enumerate(bit):
        if s=="1":
            end = i+1
            sums+=int("".join(array[start:end]))
            start=i+1
    if end==start==0:
        return int("".join(array))
    else:
        sums+=int("".join(array[start:]))
    return sums

sums = 0
for i in range(start_bit, end_bit):
    bits = str(bin(i))[3:]
    sums += get_sums(num_list, bits)

print(sums)