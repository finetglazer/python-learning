tmp=float(input())
ans=float(0)
cnt=1
while 1!=0:
    k=float((((-1)**(cnt+1))/cnt)*(tmp**cnt))
    if cnt%2==1: 
        if k<1e-5:
            break
        else:
            ans+=k
    else:
        if -k<1e-5:
            break
        else:
            ans+=k
    cnt+=1
print(f"Value of: ln(x+1) voi x = {tmp} is: {ans}")
