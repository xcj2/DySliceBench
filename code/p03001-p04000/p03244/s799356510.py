def count_char_occurrence(seq):
    # count how many times characters occur and return results as a dictionary
    ret = {}
    for char in seq:
        if char in ret:
            ret[char] += 1
        else:
            ret[char] = 1
    return ret


def accum_char_frequency(seq):
    """
    accumulate frequency of each number in a inputted sequence
    Example:
        in: [a,a,a,a,b,b,b,b,c]
        out: { 4 times: [a,b] , 1 times: [c] }
    """
    frequencies = count_char_occurrence(seq)

    ret = {}
    for char, count in frequencies.items():
        if count in ret:
            ret[count].append(char)
        else:
            ret[count] = [char]
    return ret


def main():
    _ = input()
    seq = list(map(int, input().split()))

    odd = seq[::2]
    even = seq[1::2]

    if len(set(seq)) == 1:  # when all chars are unique, return the length of even numbered chars
        print(len(even))
        return

    no_freq_odd = accum_char_frequency(odd)
    freq_odd = sorted(no_freq_odd.items(), reverse=True)
    
    no_freq_even = accum_char_frequency(even)
    freq_even = sorted(no_freq_even.items(), reverse=True)

    if len(freq_odd[0][1]) == 1 and len(freq_even[0][1]) == 1 and freq_odd[0][1] == freq_even[0][1]:
        min_change_even = len(seq)
        if len(freq_even) != 1:
            min_change_even = (len(odd) - freq_odd[0][0]) + (len(even) - freq_even[1][0])

        min_change_odd = len(seq)
        if len(freq_odd) != 1:
            min_change_odd = (len(odd) - freq_odd[1][0]) + (len(even) - freq_even[0][0])

        print(min(min_change_even, min_change_odd))
        return
    else:
        min_change = (len(odd) - freq_odd[0][0]) + (len(even) - freq_even[0][0])
        print(min_change)
        return

main()