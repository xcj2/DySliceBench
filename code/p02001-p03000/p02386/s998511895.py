


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
        global point 
        if (self.P.A[0]==self.Q.A[0] and self.P.A[5]==self.Q.A[5]):

            if self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[4]:
                point=point+1
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[3]:
                point=point+1
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[1]:
                point=point+1
            elif self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[2]:
                point=point+1
            else:
                pass
        elif (self.P.A[0]==self.Q.A[1] and self.P.A[5]==self.Q.A[4]):
            if self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[0]:
                point=point+1
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[3]:
                point=point+1
            elif self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[5]:
                point=point+1
            elif self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[2]:
                point=point+1
            else:
                pass

        elif (self.P.A[0]==self.Q.A[2]and self.P.A[5]==self.Q.A[3]):
            if self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[4]:
                point=point+1
            elif self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[0]:
                point=point+1
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[1]:
                point=point+1
            elif self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[5]:
                point=point+1
            else:
                pass

        elif (self.P.A[0]==self.Q.A[3] and self.P.A[5]==self.Q.A[2]):
            if self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[4]:
                point=point+1
            elif self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[5]:
                point=point+1
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[1]:
                point=point+1
            elif self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[0]:
                point=point+1
            else:
                pass

        elif (self.P.A[0]==self.Q.A[4] and self.P.A[5]==self.Q.A[1]):
            if self.P.A[1]==self.Q.A[0] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[5]:
                point=point+1
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[5] and self.P.A[3]==self.Q.A[0] and self.P.A[4]==self.Q.A[3]:
                point=point+1
            elif self.P.A[1]==self.Q.A[5] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[0]:
                point=point+1
            elif self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[0] and self.P.A[3]==self.Q.A[5] and self.P.A[4]==self.Q.A[2]:
                point=point+1
            else:
                pass


        elif (self.P.A[0]==self.Q.A[5] and self.P.A[5]==self.Q.A[0]):
            if self.P.A[1]==self.Q.A[3] and self.P.A[2]==self.Q.A[4] and self.P.A[3]==self.Q.A[1] and self.P.A[4]==self.Q.A[2]:
                point=point+1
            elif self.P.A[1]==self.Q.A[4] and self.P.A[2]==self.Q.A[2] and self.P.A[3]==self.Q.A[3] and self.P.A[4]==self.Q.A[1]:
                point=point+1
            elif self.P.A[1]==self.Q.A[2] and self.P.A[2]==self.Q.A[1] and self.P.A[3]==self.Q.A[4] and self.P.A[4]==self.Q.A[3]:
                point=point+1
            elif self.P.A[1]==self.Q.A[1] and self.P.A[2]==self.Q.A[3] and self.P.A[3]==self.Q.A[2] and self.P.A[4]==self.Q.A[4]:
                point=point+1
            else:
               pass
        else:
            pass
     
##実行部分######################################################################
if __name__=="__main__":
    
    #入力用関数の定義##########################################
    def in_data():
       input_text=""
       input_text=input()
       array=[]
       array=input_text.split()
       return array
    
    def in_number():
        input_n=""
        input_n=input()
        input_n=int(input_n)
        return input_n
    ###########################################################
    ###ダイスの目の入力
    
    point=0
    ob_array=[]
    i=0
    j=0
    n=in_number()
    for i in range(n):

        number=in_data()
        #一つ目のダイス
        ob_array.append(dice( number[0], number[1], number[2], number[3], number[4], number[5]))

    for i in range(n):

        for j in range(len(ob_array)):
        ##同一かどうかの判定
            if not i==j:
                det=determine(ob_array[i],ob_array[j])
                det.run()

if point==0:
    print("Yes")
else:
    print("No")
    
#################################################################################
   
