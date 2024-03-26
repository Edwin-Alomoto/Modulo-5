import random
# CLASE
class Laptop: 
  # CONSTRUCTOR
  def __init__(self,marca, procesador,memoria,costo=500,impuesto=10):
    self.marca = marca
    self.procesador = procesador
    self.memoria = memoria
    self.costo = costo
    self.impuesto = impuesto
  # METODO
  def valor_final(self):
    return self.costo + self.impuesto
  def valor_descuento(self, descuento):
    return (self.costo * descuento)/100
  #SOBRE ESCRITURA 
  def realizar_diagnostico_sistema(self):
    resultado ={
      "MARCA":f"{self.marca}",
      "PROCESADOR":f"{self.procesador}",
      "MEMORIA DISCO DURO": f"{self.memoria} gb",
      "BATERIA": "OK" if random.choice([True,False]) else "Cambiar bateria"
    }
    return resultado
  # METODO ESTATICO
  @staticmethod
  def comparar_costo(laptop1,laptop2):
    if laptop1.costo==laptop2.costo:
      return "los costo son iguales"
    else:
      return "los costo son diferente"
    
  # METODO CLASE
  @classmethod         # SOBRE ESCRIBIR EL COSTO COLOCANDO COMO NUEVO PARAMETRO
  def asus_laptop (cls,costo): #REFERENCIA A LA PROPIA CLASE
    marca = "asus"
    procesador = "i5"
    memoria = 16
    return cls (marca, procesador,memoria,costo) # CONSTRUCCION DEL OBJETO, CREANDO UN NUEVO OBJETO CON ESTAS ESPECIFICACIONES



