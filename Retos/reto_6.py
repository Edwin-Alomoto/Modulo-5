#CLASE
class auto:
  #CONSTRUCTOR 
  def __init__(self, marca,modelo,año,kilometraje=0):
    self.marca = marca
    self.modelo= modelo
    self.año=año
    self.kiometraje= kilometraje

  # METODO MOSTRAR INFORMACION 
  def mostrar_informacion():
    print("AUTO ESPECIFICACIONES: ")
    print(auto_nuevo.__dict__)
  # METODO ACTUALIZAR_KILOMETRAJE 
  def actualizar_kilometraje(kilometraje_nuevo):
    if kilometraje_nuevo> auto_nuevo.kiometraje:
      auto_nuevo.kiometraje=kilometraje_nuevo
      print(auto_nuevo.__dict__)
    else:
      print("No se puede reducir el kilometraje")
  # METODO REALIZAR VIAJE 
  def realizar_viaje(kilometraje_recorrido):
    if kilometraje_recorrido>0:
      auto_nuevo.kiometraje= kilometraje_recorrido
      print(auto_nuevo.__dict__)
    else:
      print("La cantidad de kilometro debe de ser positiva")
  # METODO ESTADO DEL AUTO
  def estado_auto():
    if auto_nuevo.kiometraje<20000:
      print("Estoy como nuevo")
    elif auto_nuevo.kiometraje>=20000 and auto_nuevo.kiometraje<=100000:
      print("ya estoy usado")
    elif auto_nuevo.kiometraje>100000:
      print("¡ya dejame descansar!")
    




auto_nuevo = auto("TOYOTA", "RAV4", 2023 )
auto.mostrar_informacion()
auto.actualizar_kilometraje(10000)
auto.realizar_viaje(30000)
auto.estado_auto()