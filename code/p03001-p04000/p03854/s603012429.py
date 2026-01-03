def readinput():
    s = input()
    return s

def compare(s):
    # dreameraser
    # dreamerase
    # dreamer
    # dream
    # eraser
    # erase
    if (s[0:11] == 'dreameraser'):
        return 11
    elif (s[0:10] == 'dreamerase'):
        return 10
    elif (s[0:7] == 'dreamer'):
        return 7
    elif (s[0:5] == 'dream'):
        return 5
    elif (s[0:6] == 'eraser'):
        return 6
    elif (s[0:5]=='erase'):
        return 5
    else:
        return 0

def main(s):
    p=0 # 比較する部分列の先頭
    while(p<=len(s)):
        if(p==len(s)):
            return True
        q = compare(s[p:])
        if(q==0):
            return False
        p += q
    return False

if __name__=='__main__':
    s = readinput()
    ans = main(s)
    if(ans == True):
        print('YES')
    else:
        print('NO')
 