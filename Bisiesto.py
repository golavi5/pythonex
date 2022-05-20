year = int(input("Introduce un año:"))

#
# Escribe tu código aquí.
#	
if year >= 1582:
    if year % 4 != 0:
        print("Commun Year")
    elif year % 100 != 0:
        print("Bisiest Year")
    elif year % 400 !=0:
        print("Commun Year")
    else:
        print("Bisiest Year")
else:
    print("No esta dentro del periodo del calendario Gregoriano")