def is_prime(num):
    if num == 2: return True
    elif num > 2:
        for i in range(2,num):
            if num % i == 0:
                return False
                break
        else:
            return True
#
# Escribe tu código aquí.
#

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()