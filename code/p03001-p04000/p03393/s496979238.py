#0. setting
CHR_A = ord("a") #97
NUM_CHR = 26
CHR_LIST = [chr(CHR_A+i) for i in range(NUM_CHR)]

def addChar(s, chr_list):
    for char in chr_list:
        if not(char in s):
            s = s+char
            break
    return s

def removeTail(s):
    for i in range(1,NUM_CHR):
        if ord(s[-1])<ord(s[-2]):
            s = s[:-1]
        else:
            s = s[:-1]
            last_s = s[-1]
            s = s[:-1:1]
            candidate = [chr(i) for i in range(ord(last_s)+1, CHR_A+NUM_CHR)]
            s = addChar(s, candidate)
            break
    return s

def main():
    #1. input
    s = input()

    #sp. output -1 if S='zyx...a'
    if s == ''.join(CHR_LIST[::-1]):
        print(-1)
    
    
    #2. add next char if |S| <= 25
    elif len(s) <= 25:
        s = addChar(s, CHR_LIST)
        print(s)
    
    
    #3. jump next step if |S| == 26
    else:
        s = removeTail(s)
        print(s)
    
if __name__ == "__main__":
    main()