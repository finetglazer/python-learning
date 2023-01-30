def square_num(a):
    ans=[]
    k=int(a**(1/2))
    for i in range(0,k+1):
        ans.append(i**2)
    print(ans)
a=int(input())
square_num(a)
    