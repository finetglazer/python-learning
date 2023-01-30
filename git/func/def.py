# def name(vars):
#     lenh
#     return or not
def hello():
    print("hello")


hello()


def hello(a):
    print(f"hello {a}")


a = "my love"
hello(a)


def giaithua(a):
    tmp = 1
    for i in range(1, a+1):
        tmp *= i
    return tmp


x = 5
print(giaithua(5))


def vi_du(a, b="Python"):
    print(a, b)


vi_du("Lap trinh")
vi_du("Lap trinh", "Java")
# Lap trinh Python
# Lap trinh Java


def upper(text):
    return text.upper()


def lower(text):
    return text.lower()


def convert(func):
    # storing the function in a variable
    result = func("Hi, I am higher order function and I call another function as my arguments.")
    print(result)


convert(upper)
convert(lower)
# lambda

# lambda arguments: expression

sq = lambda a: a*a 
print(sq(5))

power = lambda a, n: a**n
print(power(5,2))

#filter and map

# filter pure the lst by the cond
lst=[1,2,4,5,6]
sq= list(filter(lambda x: x%2==0, lst))
print(sq) 

# make the new list by the cal by the func 

sql=list(map(lambda x: x**2,lst))
print(sql)