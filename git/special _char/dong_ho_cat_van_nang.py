size=int(input())
i=1
while i<=2*size:
    if i <= size:
        tmp = 1 
        while tmp < i:
            print(" ",end="")
            tmp+=1
        cnt=1
        while cnt <= size - i + 1: 
            print("*",end=" ")
            cnt+=1
        print("")     
    else:
        tmp=1
        while tmp < 2 * size - i + 1:
            print(" ",end="")
            tmp+=1
        cnt=1
        while cnt <= i - size :
            print("*",end=" ")
            cnt+=1
        print("")
    i+=1