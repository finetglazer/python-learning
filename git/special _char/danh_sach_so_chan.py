tmp=0
lst=[]
while 1!=0:
    tmp=int(input())
    if tmp%2==0:
        lst.append(tmp)
    elif tmp<0:
        break
print(lst)