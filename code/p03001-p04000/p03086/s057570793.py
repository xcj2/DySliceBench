def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        for j in range(len(S)+1):
            ans = max(ans, cal_ACGT(S[i:j]))
    print(ans)

def cal_ACGT(substr):
    if (is_ACGT(substr)):
        return len(substr)
    else:
        return 0

def is_ACGT(substr):
    flag = []
    for i in range(len(substr)):
        if(substr[i] == "A"):flag.append(True)
        elif(substr[i] == "C"):flag.append(True)
        elif(substr[i] == "G"):flag.append(True)
        elif(substr[i] == "T"):flag.append(True)
        else:flag.append(False)
    return all(flag)

main()
