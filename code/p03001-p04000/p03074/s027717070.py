
def get_input():
    N,K = [int(_) for _ in input().split()]
    S = [int(_) for _  in list(input())]
    return N,K,S

def solve(N,K,S):
    length = len(S)
    array = count_array(S)
    start_char = S[0]
    ans = find_max(array,K,start_char)
    return ans

def find_max(array,K,start_char):
    if start_char ==0 and len(array) <= 2 * K:
        return sum(array)
    elif start_char == 1 and len(array) <=2 * K+1 :
        return sum(array)
    else:
        if start_char == 0:
            start,end = 1,2*K+2
        else:
            start,end = 0,2*K+1
        idx = 0
                    
        current_sum = sum(array[start:end])
        ret = [current_sum]
        if start_char == 0:
            ret.append(sum(array[0:2*K]))
        ret.append(sum(array[-2*K:]))
        while(1):
            start+=2
            end+=2
            if end > len(array):
                break
            current_sum = current_sum- sum(array[start-2:start]) + sum(array[end-2:end])
            ret.append(current_sum)
    return max(ret)
            

def count_array(S):
    array = []
    cur_char = S[0]
    cur_val = 1
    for char in S[1:]:
        if cur_char != char:
            array.append(cur_val)
            cur_char = char
            cur_val = 1
        else:
            cur_val+=1
    array.append(cur_val)

    return array





if __name__ == "__main__":
    N,K,S = get_input()
    ans = solve(N,K,S)
    print(ans)