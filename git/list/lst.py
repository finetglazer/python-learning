a=[1,2,3,4,5]
print(a[2:4])
b=a[1:2:3]
# 1
print(b)
#append add 1 member into the index last
a.append([2,3])
print(a)
#extend add many members into the last
b.extend([1,3,4])
print(b)
#insert format (index,val)
a.insert(2,4)
print(a)
# del is the order and the format like the slice
del a[3:]
print(a)
