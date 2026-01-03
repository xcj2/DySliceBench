"""
def bs(num_array, max_element, min_element):
    from collections import deque
    if(num_array == max_element - min_element + 1):
        que = deque(deque([i for i in range(min_element, max_element+1, 1)]))
        return que
    else:        
        # If min_element is not used
        que = deque([deque([])])
        que.extend(bs(num_array, max_element, min_element + 1))
        # IF min_element is used
        subset_yes = bs(num_array-1, max_element, min_element + 1)
        for e in subset_yes:
            e.appendleft(min_element)
        
        que.extendleft(subset_yes)
        return que
"""
def solve(S):
    from itertools import combinations
    from collections import deque
    n = len(S)
    answer = 0
    for i in range(n):
        for item in combinations(list(range(1, n, 1)), i):
            char_list = [c for c in S]
            que = deque(item)
            while que:
                index = que.pop()
                char_list.insert(index, " ")
            split_s = ""
            for c in char_list:
                split_s += c
            #print(split_s)
            answer += sum(map(int, split_s.split()))
    return answer

def main():
    S = input()

    print(solve(S))
#print(solve("125"))
#print(solve("9999999999"))
main()