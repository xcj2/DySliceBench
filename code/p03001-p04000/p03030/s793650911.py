from operator import itemgetter

def input_list(num,args):
    for i in range(num):
        S,P = input().split()
        P=int(P)
        if 1<=len(S)<=10 and S.islower()==1 and S.isalpha()==1 \
           and 0<=P<=100 and isinstance(P,int)==1:
            args.append([S,P])
        else :
            print("ERROR")
            exit()



def sort_list(*args):
    tmp=sorted(args,key=itemgetter(1),reverse=1)
    dict_sorted=sorted(tmp,key=itemgetter(0))

    return dict_sorted


def check_list(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    if len(seq) != len(unique_list):
        print("ERORR")
        exit()
    # else :                                                                                         
    #     print("restaurant is ok.")           



def main():
    # restaurant=[['N1',88],['N2',85],['N3',92],['N7',21],['N4',34],['N8',45],['N2',24],['N2',35]]   
    # num=8                                                                                          

    num=int(input())
    if 1<=num<=100:
        # [[] for i in range(5)]                                                                     
        restaurant=[]
        input_list(num,restaurant)

        check_list(restaurant)

        # print(restaurant)                                                                          
        restaurant_sorted=sort_list(*restaurant)

        for i in range(num):
            for j in range(num):
                if restaurant_sorted[i][1]==restaurant[j][1]:
                    print(j+1)
    else :
        print("ERORR")
        exit()

if __name__ == "__main__":
    main()

