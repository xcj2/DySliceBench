import re

class bintree():
    def __init__(self, str1):
        self.str1 = str1
        if self.str1[1] != ",":
            c = 0
            counter = 0
            for s in str1[1:]:
                counter += 1
                if s == "(":
                    c += 1
                elif s == ")":
                    c -= 1
                if c == 0:
                    break
            self.left = bintree(str1[1:counter+1])
                
            #match1 = re.search("\((\(.*\)),.*\)",str1)
            #if match1 != None:
            #    self.left = bintree(str(match1.group(1)))
        else:
            self.left = ""
        if self.str1[-2] != ",":
            str1 = str1[0]+str1[1+len(str(self.left)):]
            match2 = re.search("\(,(\(.*\))\)",str1)
            if match2 != None:
                self.right = bintree(str(str1[2:-1]))
        else:
            self.right = ""
    def __str__(self):
        return self.str1
        
def inter(bin1, bin2):
    if bin1.left != "" and bin2.left != "":
        strleft = inter(bin1.left, bin2.left)
    else:
        strleft = ""
    if bin1.right != "" and bin2.right != "":
        strright = inter(bin1.right, bin2.right)
    else:
        strright = ""
    return "(" + strleft + "," + strright + ")"

def union(bin1, bin2):
    if bin1.left != "" or bin2.left != "":
        if bin1.left == "":
            strleft = str(bin2.left)
        elif bin2.left == "":
            strleft = str(bin1.left)
        else:
            strleft = union(bin1.left, bin2.left)
    else:
        strleft = ""
    if bin1.right != "" or bin2.right != "":
        if bin1.right == "":
            strright = str(bin2.right)
        elif bin2.right == "":
            strright = str(bin1.right)
        else:
            strright = union(bin1.right, bin2.right)
    else:
        strright = ""
        #print("(" + strleft + "," + strright + ")")
    return "(" + strleft + "," + strright + ")"



while True:
    
    try:
        inputs = map(str,input().split())
        order = next(inputs)
        if order == "i":
            t1 = bintree(next(inputs))
            t2 = bintree(next(inputs))
            #print(t1.left,t1.right)
            print(inter(t1, t2))#  == "((((((,),),),),),)")
            
        elif order == "u":
            t1 = bintree(next(inputs))
            t2 = bintree(next(inputs)) 
            #print(t1.left,t1.right)
            #print(t1.left,t1.right)
            print(union(t1,t2))# == "((((,),(,)),((,),(,))),(((,),(,)),((,),(,))))")
    except EOFError as exception:
        break
