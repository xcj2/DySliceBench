def charToInt(c):
    return ord(c) - ord("a")
 
def stringToFlags(s):
    t = [False for i in range(26)]
    for i in range(len(s)):
        t[charToInt(s[i])] = True
    return t
 
def B(n, s):
    max = 0
    for i in range(1, n):
        xflags = stringToFlags(s[0:i])
        yflags = stringToFlags(s[i:n])
        
        count = 0
        for i in range(26):
            if xflags[i] and yflags[i]:
                count += 1
                if count > max:
                    max = count
    return max
 
n = int(input())
s = input()
print(B(n, s))