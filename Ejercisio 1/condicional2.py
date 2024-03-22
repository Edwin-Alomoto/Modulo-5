# IMPORTACION DE METODO
import random
aleatorio_uno = random.randint(1,9)
aleatorio_dos = random.randint(1,9)
# CONDICIONAL 
if aleatorio_uno ==4:
  print("te ganaste un chupete")
elif aleatorio_uno==8:
  print("te ganaste un balon")
elif aleatorio_uno==3 and aleatorio_dos==7:
  print ("te ganaste un televisor")
else:
  print("perdiste!!!")
