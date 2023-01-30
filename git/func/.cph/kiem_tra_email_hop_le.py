def verify_email(s):
    if (s[0]>='a' and s[0]<='z') or (s[0]>='A' and s[0]<='Z'):
        cnt1=s.count('@')
        cnt2=s.count('.')
        if cnt1!=1 or cnt2!=1:
            return False
        else:
            id1=s.index('@')
            id2=s.index('.')
            if id1>id2:
                return False
            else :
                if id2 == len(s)-1:
                    return False
                else:
                    return True
    else :
        return False   


email=input()
if verify_email(email)==True:
    print("Valid")
else:
    print("Invalid")