def pfnum(a,b):
    print(f"Below are all perfect numbers between {a} and {b}:")
    for i in range(a,b+1,1):
        tmp=int(1)
        for j in range(2,int(i**(1/2))+1,1):
            if i%j==0:
                tmp+=j
                tmp+=(i/j)
        tmp=int(tmp)
        if tmp == i and i!=1:
            print(f"{tmp} is a perfect number")
        
a=int(input())
b=int(input())
pfnum(a,b)