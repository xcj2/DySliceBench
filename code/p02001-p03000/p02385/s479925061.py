#ダイスオブジェクト#############################################################
class dice():
    
    def __init__(self,a,b,c,d,e,f):
        self.A=[a,b,c,d,e,f]
#判定オブジェクト###############################################################
class determine():

    def __init__(self,P,Q):
        self.P=P
        self.Q=Q
    def run(self):
  
        if (self.P.A[0]==self.Q.A[0] and self.P.A[5]==self.Q.A[5]):

            if self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[4]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[3]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[1]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[2]:
                print("Yes")
            else:
                print("No")
        elif (self.P.A[0]==self.Q.A[1] and self.P.A[5]==self.Q.A[4]):
            if self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[0]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[3]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[5]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[2]:
                print("Yes")
            else:
                print("No")

        elif (self.P.A[0]==self.Q.A[2]and self.P.A[5]==self.Q.A[3]):
            if self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[4]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[0]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[1]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[5]:
                print("Yes")
            else:
                print("No")

        elif (self.P.A[0]==self.Q.A[3] and self.P.A[5]==self.Q.A[2]):
            if self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[4]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[5]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[1]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[0]:
                print("Yes")
            else:
                print("No")

        elif (self.P.A[0]==self.Q.A[4] and self.P.A[5]==self.Q.A[1]):
            if self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[5]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[3]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[0]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[2]:
                print("Yes")
            else:
                print("No")


        elif (self.P.A[0]==self.Q.A[5] and self.P.A[5]==self.Q.A[0]):
            if self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[2]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[1]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[3]:
                print("Yes")
            elif self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[4]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
     
##実行部分######################################################################
if __name__=="__main__":
    #入力用関数の定義##########################################
    def in_data():
       input_text=""
       input_text=input()
       array=[]
       array=input_text.split()
       return array
    ###########################################################
    ###ダイスの目の入力
    
    number=in_data()
    #一つ目のダイス
    ob1=dice( number[0], number[1], number[2], number[3], number[4], number[5])

    number=in_data()
    #二つ目のダイス
    ob2=dice( number[0], number[1], number[2], number[3], number[4], number[5])

    ##同一かどうかの判定
    det=determine(ob1,ob2)
        # method
    det.run()
#################################################################################
   
