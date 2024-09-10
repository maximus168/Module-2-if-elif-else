first=input('введите 1-е число  ')
second=input('введите 2-е число  ')
third=input('введите 3-е число  ')
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)