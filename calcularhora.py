""" hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
min_fin = (mins + dura) % 60
totalhours = (mins + dura) // 60 #int((mins + dura) / 60)
hour_fin = (hour + totalhours) % 24

print (str(hour_fin)+":"+str(min_fin)) """

dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1],end="")

print("a","b","c",sep="sep")

foo = (1,2,3)
foo.index(1)

print(3+6)

def func(inp=2,out=3):
    return inp * out

print(func(out=2))

my_list = [1,2]
for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
