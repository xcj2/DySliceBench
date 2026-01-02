def cross(s):
    if s[0]==s[4]==s[8] and s[0]!="s":
        print(s[0])
        return True
    elif s[2]==s[4]==s[6] and s[2]!="s":
        print(s[2])
        return True
    else:
        return False

def side(s):
    for i in range(0,len(s),3):
        if s[i]==s[i+1]==s[i+2] and s[i]!="s":
            print(s[i])
            return True
    return False
def ver(s):
    for i in range(3):
        if s[i]==s[i+3]==s[i+6] and s[i]!="s":
            print(s[i])
            return True
    return False


while True:
    try:
        s=list(map(str,input()))               
    except EOFError:
        break
    if cross(s)==side(s)==ver(s)==False:
        print("d")

    
