#coding-utf8
#Complete Binary Tree

def parent(i):
    return i//2

def left(i):
    return i*2

def right(i):
    return i*2+1

def main():
    H=int(input())
    a = [0] + list(map(int, input().split()))

    for i in range(H):
        i+=1
        print("node "+str(i)+": key = "+str(a[i])+", ",end="")
        if(parent(i)):
            print("parent key = "+str(a[parent(i)])+", ",end="")
        if(left(i)<=H):
            print("left key = "+str(a[left(i)])+", ",end="")
        if(right(i)<=H):
            print("right key = "+str(a[right(i)])+", ",end="")
        print()

    return 0

if __name__ == "__main__":
    main()

