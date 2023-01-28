sum=int(input())
ans=0
while (ans+1)*ans/2 <= sum:
    ans+=1
print(ans)