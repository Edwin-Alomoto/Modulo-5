#LISTAS
planetas = ["mercurio","venus","tierra","marte","jupiter","saturno","uranio","neptuno"]
# print(planetas)
# print(planetas[1])
# #SUBLISTA
# print(planetas[1:6])
# print(planetas[1:])
# #CUANTO CALORES EN LA LISTA
# print(len(planetas))

#LISTAS DE NUMERO 
gravedad_en_planetas = [0.378,0.907,1,0.377,2.36,0.916,0.889,1.12]
peso_bus=124054 #NEWTON, EN LA TIERRA
print (f"En la tierra , un autobus de dos pisos pesa {peso_bus} N")
print (f"En mercurio , un auto de dos piso pesa {peso_bus*gravedad_en_planetas[0]}")

# VALORES MINIMO Y MAXIMOS
print(f"Lo mas liviano que seria un autobus en el sistema solar es: {peso_bus* min(gravedad_en_planetas)} N")
print(f"Lo mas pesado que seria un autobus en el sistema solar es: {peso_bus* max(gravedad_en_planetas)} N")