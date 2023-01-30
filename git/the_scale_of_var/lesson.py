a = "dididid"

def vi_du():
   print(a)

vi_du()
print(a)
# dididid
# dididid
a = "tusena"

def vi_du():
    a = "a"
    print(a)

vi_du()
print(a)
# a
# tusena
a = 1

def vi_du():
    global a
    a = a + 99
    print(a)

vi_du()
print(a)
# 100
# 100
# Create a string: name
name = "Java"

# Define change_name() function
def change_name():
    """Change the value of the variable name."""
    global name
    name="python"

# Print name before function call
print(name)
# Call change_name()
change_name()

# Print name after function call
print(name)
#Java
#python
global x="vl"



# muốn khởi tạo biến toàn cục khai báo global