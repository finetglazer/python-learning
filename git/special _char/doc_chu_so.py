def convert_text(a):
    res=""
    str=['0',"one","two",'three','four','five','six','seven','eight','nine']
    for i in range(0,len(a),1):
        ind=int(a[i])
        res+=str[ind]
    tmp=" "
    res=tmp.join(res)
    return res
a=input()
ans=convert_text(a)
print(ans)