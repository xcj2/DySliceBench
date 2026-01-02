def InputData():
    
    sequence_len = int(input())
    sequence = list(map(int, input().split()))

    description_len = int(input())
    description = list(map(int, input().split()))

    return sequence_len, sequence, description_len, description

def Solve(sequence_num, description_value, sequence, sequence_len):
    if description_value == 0: return True
    elif sequence_num >= sequence_len or description_value > sum(sequence): return False
    res = Solve(sequence_num + 1, description_value, sequence, sequence_len) or \
    Solve(sequence_num + 1, description_value - sequence[sequence_num], sequence, sequence_len)
    
    return res

def main():
    [sequence_len, sequence, description_len, description] = InputData()
    for i in description:
        if Solve(0, i, sequence, sequence_len):
            print("yes")
        else:
            print("no")
        

if __name__ == "__main__":
    main()

    
