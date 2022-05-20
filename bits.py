a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c+d+e)

mylist=[1,2,3]
for v in range(len(mylist)):
    mylist.insert(1,mylist[v])

print(mylist)