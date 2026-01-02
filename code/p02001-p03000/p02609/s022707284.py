def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()
S=one_str()

bit_count = S.count("1")
S_num = int(S,2)
S_min = S_num % (bit_count-1) if bit_count-1!=0 else 0
S_plu = S_num % (bit_count+1)




# calc_dict = {i:-1 for i in range(10000)}
# res_dict =  {i:-1 for i in range(10**4)}

# for i in range(1, 10000):
#     if calc_dict[i]==-1:
#         calc_dict[i] = bin(i).count("1")

#     res_dict[i] = i%calc_dict[i]+1

def mods(temp, count):
    count+=1
    if temp!=0:

#         if temp in res_dict:
#             return count+res_dict[temp]
        
#         if temp not in calc_dict:
#             calc_dict[temp]= bin(temp).count("1") 
        count = mods(temp%bin(temp).count("1") , count)

    return count

for i in range(N):
    if S[i]=="0":
        part = pow(2, (N-i-1), bit_count+1)
        num = (S_plu + part ) % (bit_count+1)
        print(mods(num, 0))
    else:
        if S_num == 2**(N-i-1):
            print(0)
            continue
        part = pow(2, (N-i-1), bit_count-1)
        num = (S_min - part)%(bit_count-1)
        print(mods(num, 0))


