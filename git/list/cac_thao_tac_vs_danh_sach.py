n = int(input())
list = []
tmp=""
for i in range(n):
    tmp = input()
    s = tmp.split(" ")
    if len(s) == 1:
        if s[0] == "print":
            print(list)
        elif s[0] == "sort":
            list.sort()
        elif s[0] == "pop":
            if len(list) != 0:
                list.pop()
        else:
            list.sort(reverse=True)
    elif len(s) == 2:
        if s[0] == 'remove':
            list.remove(int(s[1]))
        else:
            list.append(int(s[1]))
    else:
        if s[0] == 'insert':
          list.insert(int(s[1]), int(s[2]))
