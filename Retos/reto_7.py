#CLASE
class auto:
  #CONSTRUCTOR 
  def __init__(self, marca,modelo,año,kilometraje=0):
    self.marca = marca
    self.modelo= modelo
    self.año=año
    self.kiometraje= kilometraje

# RETO 7 
  @classmethod
  def autos_toyota (cls): #REFERENCIA A LA CLASE
    marca="TOYOTA"
    modelo="RAV4"
    año=2024 # CONSTRUCCION DEL OBJETO, CREANDO UN NUEVO OBJETO CON ESTAS ESPECIFICACIONES
    return cls (marca,modelo,año)

  @classmethod
  def autos_toyota_kilometraje (cls, kilometraje): #REFERENCIA A LA CLASE
    marca="TOYOTA"
    modelo="RAV4"
    año=2024 # CONSTRUCCION DEL OBJETO, CREANDO UN NUEVO OBJETO CON ESTAS ESPECIFICACIONES
    return cls (marca,modelo,año, kilometraje)

  @staticmethod
  def comparar_kilometraje (auto1,auto2):
    if auto1==auto2:
      print("El kilometraje son iguales")
    else:
      print("El kilometraje son diferente")

  @staticmethod 
  def comparar_año (auto1,auto2):
    if auto1==auto2:
      print("Son del mismo año")
    else:
      print("Son años diferente")
 
auto_nuevo = auto.autos_toyota()
print(auto_nuevo.__dict__)
print("\n")

for i in range (20,30):
  auto_nuevo = auto.autos_toyota_kilometraje(i)
  print(auto_nuevo.__dict__)
print("\n")

auto_kia = auto("KIA", "SPORTAGE", 2023)
auto_ford = auto("FORD", "CROSSOVER", 2022)
print(auto.comparar_año(auto_kia,auto_ford))

auto_kia = auto("KIA", "SPORTAGE", 2023,kilometraje=100)
auto_ford = auto("FORD", "CROSSOVER", 2022,kilometraje=20000)
print(auto.comparar_kilometraje(auto_kia,auto_ford))
