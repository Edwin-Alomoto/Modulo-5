#INGRESO DE DATOS 
conductor = int(input("La velocidad que maneja el conductor es de : "))
# VELOCIDADES DE LOS TRES PAISES
#ECUADOR
print("Para Ecuador")
if conductor <10:
  print("Está por debajo de lo permitido aceleré por favor\n")
elif conductor>=10 and conductor<=50:
  print("Esta viajando en zona urbana\n")
elif conductor>=51 and conductor<=70:
  print("Esta viajando en zona rural\n")
elif conductor>=71 and conductor <=90:
   print("Esta viajando en zona perimentral\n")
else:
  print("Está excediendo los límites establecido bajé la velocidad!!\n")

  #COLOMBIA 
print("Para Colombia")
if conductor <10:
  print("Está por debajo de lo permitido aceleré por favor\n")
elif conductor>=10 and conductor<=30:
  print("Esta viajando en zona urbana\n")
elif conductor>=31 and conductor<=80:
  print("Esta viajando en zona rural\n")
elif conductor>=81 and conductor <=100:
   print("Esta viajando en zona perimentral\n")
else:
  print("Está excediendo los límites establecido bajé la velocidad!!\n")

  #PERU
print("Para Peru")
if conductor <10:
  print("Está por debajo de lo permitido aceleré por favor\n")
elif conductor>=10 and conductor<=40:
  print("Esta viajando en zona urbana\n")
elif conductor>=41 and conductor<=60:
  print("Esta viajando en zona rural\n")
elif conductor>=61 and conductor <=120:
   print("Esta viajando en zona perimentral\n")
else:
  print("Está excediendo los límites establecido bajé la velocidad!!\n")