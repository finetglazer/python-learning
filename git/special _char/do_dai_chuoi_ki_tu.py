str=input()
def length(str):
    l=0
    for i in str:
        l+=1
    return l
print(f"Count string length with for loop: {len(str)}")
print(f"Get string length with Python len() function: {length(str)}")