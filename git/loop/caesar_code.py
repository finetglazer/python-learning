text = input() #Nhận đoạn văn bản rõ
k = int(input()) # Nhận khóa nhập vào từ bàn phím, ép kiểu về số nguyên
# chr(ord(x)+x%26)
# a= chr(ord("a") + k)
# print(a)
# func
ans=""
for i in text:
  if 65<=ord(i)<=90:
    if ord(i) + k > 90 :
      ans += chr((ord(i) + k) % 90 + 64)
    else :
      ans += chr((ord(i) + k))
  elif 97<=ord(i)<= 122:
    if ord(i) + k > 122 :
      ans += chr((ord(i) + k) % 122 + 96)
    else :
      ans += chr((ord(i) + k))
  else:
    ans+=i
print(ans)