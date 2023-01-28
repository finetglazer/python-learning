def giaiThua(n):
    gt=1
    for i in range(1,n+1):
        gt*=i
    return gt

x=int(input())
res=0
for i in range(0,31):
    res+=(x**i)/giaiThua(i)
res/=(res+ 1)
print(res)