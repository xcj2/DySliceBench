def main():
    s=input()
    a=int(s[0])
    b=int(s[1])
    c=int(s[2])
    d=int(s[3])
    ansst=""
    def rec3(ans):
        if ans+d==7:
            ansst="+"+str(d)+"=7"
            return ansst
        if ans-d==7:
            ansst="-"+str(d)+"=7"
            return ansst
        return ""
    def rec2(ans):
        ansst=rec3(ans+c)
        if ansst:
            ansst="+"+str(c)+ansst
            return ansst
        ansst=rec3(ans-c)
        if ansst:
            ansst="-"+str(c)+ansst
            return ansst
        return ""

    def rec(ans):
        ansst=rec2(ans+b)
        if ansst:
            ansst=str(a)+"+"+str(b)+ansst
            return ansst
        ansst=rec2(ans-b)
        if rec2(ans-b):
            ansst=str(a)+"-"+str(b)+ansst
            return ansst
        return False
    print(rec(a))
    
if __name__=='__main__':
    main()
