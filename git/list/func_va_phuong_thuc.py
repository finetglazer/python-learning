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
# any and all
a=float(input())
b=float(input())
c=float(input())
tam_giac=[a>0, b>0, c>0, a+b>c, a+c>b,b+c>a]
tam_giac_vuong=[a**2 + b**2 == c**2 , a**2 + c**2 == b**2 ,b**2 + c**2 == a**2]
tam_giac_can_deu=[a==b, b==c, c==a]
tam_giac_tu=[a**2 + b**2 < c**2, a**2 + c**2 < b**2, b**2 + c**2 < a**2]

if (all(tam_giac)):
  if (any(tam_giac_vuong)):
    print("Right triangle !")
  elif(all(tam_giac_can_deu)):
    print("Equilateral triangle !")
  elif (any(tam_giac_can_deu)):
    print("Isosceles triangle !")
  elif (any(tam_giac_tu)):
    print("Obtuse triangle !")
  else:
    print("Acute triangle !")
else:
  print("Not a Triangle !")