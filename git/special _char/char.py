'''
'd'
Số nguyên có dấu
print('%d' %(-100))
>>> -100
'i'
Số nguyên có dấu
print('%i' %(-100))
>>> -100
'o'
Giá trị dạng bát phân (octan)
print('%o' %(20))
>>> 24
'u'
Giống với ký tự 'd'.
print('%u' %(-100))
>>> -100
'x'
Giá trị hệ 16 có dấu (viết thường)
print("%5x"% (47))
>>> 2f
'X'
Giá trị hệ 16 có dấu (viết hoa)
print("%5.4X"% (47))
>>> 002F
'e'
Định dạng số mũ cho số thực dấu chấm động (viết thường)
print("%9.2e"% (312.087))
>>> 3.12e+02
'E'
Định dạng số mũ cho số thực dấu chấm động (viết hoa)
print("%9.2E"% (312.087))
>>> 3.12E+02
'f'
Định dạng số thực dạng thập phân
print('%f' %(100.21))
>>> 100.210000
'F'
Định dạng số thực dạng thập phân
print('%F' %(100.21))
>>> 100.210000
'g'
Định dạng số thực dấu chấm động. Sử dụng định dạng số mũ viết thường nếu số mũ nhỏ hơn -4 hoặc nhỏ hơn độ chính xác
print('%g' %(3e9))
>>> 3e+09
'G'
Định dạng số thực dấu chấm động. Sử dụng định dạng số mũ viết hoa nếu số mũ nhỏ hơn -4 hoặc nhỏ hơn độ chính xác
print('%G' %(3e9))
>>> 3E+09
'c'
Một ký tự (nhận vào một giá trị số nguyên hoặc một ký tự)
print('%c' %('a'))
>>> a
'r'
Chuỗi ký tự (chuyển đổi từ bất kỳ đối tượng Python nào bằng hàm repr()
print('%r' %('Python'))
>>> 'Python'
's'
Chuỗi ký tự (chuyển đổi từ bất kỳ đối tượng Python nào bằng hàm str()
print('%s' %('Python'))
>>> Python
'a'
Chuỗi ký tự (chuyển đổi từ bất kỳ đối tượng Python nào bằng hàm ascii()
print('%a' %('Python cơ bản'))
>>> 'Python c\u01a1 b\u1ea3n'
'%'
Không có tham số nào được chuyển đổi, trả về kết quả là ký tự dấu phần trăm '%'
print('%')
>>> %
'''
# :<
# Căn lề bên trái với một lượng khoảng trống nhất định
# print("There are {:<8} chickens".format(49))
# >>> There are 49       chickens
# :>
# Căn lề bên phải với một khoảng trống nhất định
# print("There are {:>8} chickens".format(49))
# >>> There are       49 chickens
# :^
# Căn lề chính giữa với một khoảng trống nhất định
# print("There are {:^8} chickens".format(49))
# >>> There are    49    chickens
# :=
# Đặt dấu ở vị trí bên trái xa nhất
# print("It's {:=10} degrees".format(-10))
# >>> It's -       10 degrees
# :+
# Chỉ định kết quả là số dương hay số âm
# print("It is {:+} and {:+} degrees".format(-3, 7))
# >>> It is -3 and +7 degrees
# :-
# Chỉ định cho các kết quả là số âm
# print("It is {:-} and {:-} degrees celsius.".format(-3, 7))
# >>> It is -3 and 7 degrees celsius.
# :
# Sử dụng một khoảng trắng để thêm khoảng trắng trước các giá trị số dương
# print("It is {: } and {: } degrees celsius.".format(-3, 7))
# >>> It is -3 and  7 degrees celsius.
# :,
# Sử dụng dấu phẩy làm dấu phân tách hàng nghìn
# print("Universe is {:,} years old.".format(13800000000))
# >>> Universe is 13,800,000,000 years old.
# :_
# Sử dụng dấu gạch dưới làm dấu phân tách hàng nghìn
# print("The universe is {:_} years old.".format(13800000000))
# >>> The universe is 13_800_000_000 years old.
# :b
# Định dạng số nhị phân
# print("Binary of {0} is {0:b}".format(5))
# >>> Binary of 5 is 101
# :c
# Chuyển đổi giá trị sang các bộ ký tự unicode tương ứng
# print('It is {:c}'.format(64))
# >>> It is @
# :d
# Định dạng số thập phân
# print("There are {:d} chickens.".format(0b101))
# >>> There are 5 chickens.
# :e
# Định dạng số học, với ký tự e viết thường
# print("There are {:e} chickens.".format(5))
# >>> There are 5.000000e+00 chickens.
# :f
# Cố định định dạng số thập phân
# print("Price is {:.2f}$".format(45))
# >>> Price is 45.00$
# :g
# Định dạng chung
# print('{:g}'.format(3.14159))
# >>> 3.14159
# :o
# Định dạng số bát phân
# print("Octal of {0} is {0:o}".format(10))
# >>> Octal of 10 is 12
# :x
# Định dạng số hệ 16
# print("Hexadecimal of {0} is {0:x}".format(255))
# >>> Hexadecimal of 255 is ff
# :n
# Định dạng số
# print('{:n}'.format(359))
# >>> 359
# :%
# Định dạng số phần trăm
# print("Score is {:.0%}".format(0.25))
# >>> Score is 25%