gallon = 3.785411784 #lts
mile = 1.609344 #km

def liters_100km_to_miles_gallon(liters):
    conv = (gallon * (100 / liters))/mile
    return conv
#
# Escribe tu código aquí.
#

def miles_gallon_to_liters_100km(miles):
    conv = 100 / ((miles*mile)/gallon)
    return conv
#
# Escribe tu código aquí.
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
