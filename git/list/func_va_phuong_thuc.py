lst=[5,4,2,6,5,7]
#sort 
lst.sort()
lst.sort(reverse=True)
print(lst)
""" different from c++"""
# sum 
print(sum(lst))
# copy
lst1=lst.copy()
print(lst1)
#find 
# 1. in and not in
if(5 in lst):
    print('yes')
if(5 not in lst):
    print('yes')
# 2. index
print(lst.index(5)) # first val appear
# count
cnt =lst.count(5)
print(cnt)
# max min and sum
greatest = max(lst)
print(greatest)
smallest = min(lst[0::2])
print(smallest)
s=sum(lst[1::3])
print(s)
