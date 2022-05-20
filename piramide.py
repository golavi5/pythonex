blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	
i = 0
height = 0
row = 1
sum = 1
while sum <= blocks:
    if i > row:
        height += 1
        row = i
        sum += row
        i = 0
    else:
        i += 1
    
print("La altura de la pirámide:", height)
