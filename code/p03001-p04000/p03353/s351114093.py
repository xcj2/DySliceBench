mojiretu = input()
K = int(input())

def n_th_singleton(n, moji):
    min = moji[0]
    min_nth_itimoji = []
    if n >= 2:
        nth_soeji = [j for j in range(len(moji)) if hikaku(moji[j], moji, n_th_singleton(n-1, moji))]
        #print(nth_soeji)
        min = moji[nth_soeji[0]]
        for i in nth_soeji:
            if (min >= moji[i]):
                min = moji[i]
                min_nth_itimoji.append(i)
    else:
        for i in range(len(moji)):
            if min >= moji[i]:
                min = moji[i]
                min_nth_itimoji.append(i)
    #print(min_nth_itimoji)
    return min_nth_itimoji

def hikaku(singleton, original_moji, soeji_list):
    for j in soeji_list:
        if singleton <= original_moji[j]:
            return False
    return True

def solution(moji, num):
    sucesseive_length = 0
    n = 1
    while sucesseive_length < num:
        n_list = n_th_singleton(n, moji)
        n_sorted_submoji_list = [moji[i:] for i in n_list]
        n_sorted_submoji_list.sort()
        not_choufuku_list = []
        #print(n_sorted_submoji_list)

        j = 0
        while j < len(n_sorted_submoji_list):
            for k in range(1, len(n_sorted_submoji_list[j])+1):
                if (n_sorted_submoji_list[j][:k] not in not_choufuku_list) and sucesseive_length < num:
                    sucesseive_length += 1
                    not_choufuku_list.append(n_sorted_submoji_list[j][:k])
                    #print(not_choufuku_list)
            if sucesseive_length == num:
                    #print(not_choufuku_list)
                return not_choufuku_list[-1]
            j += 1
        #print(sucesseive_length)
        n += 1


print(solution(mojiretu, K))