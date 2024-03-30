from laptop import Laptop #IMPORTAR
class Laptop_Gaming(Laptop): #ESTA CLASE VA HEREDAR DE LA CLASE LAPTOP

  #CONSTRUCTOR HERENCIA DE LA CLASE LAPTOP
  def __init__(self, marca, procesador, memoria, tarjeta_grafica, costo=500, impuesto=10):
    super().__init__(marca, procesador, memoria, costo, impuesto)
    self.tarjeta_grafica = tarjeta_grafica
  
  #SOBRE ESCRIBIR EL METODO PARA MOSTRAR
  def __str__(self) -> str:
    return f" marca: {self.marca} \n procesador: {self.procesador} \n memoria: {self.memoria} \n tarjeta_grafica: {self.tarjeta_grafica} \n costo: {self.costo} \n impuesto: {self.impuesto} \n"
    
  #AGREGAR LO QUE NO ESTA EN LA CLASE PADRE
  def realizar_diagnostico_sistema(self):
    resultado_diagnostico = super().realizar_diagnostico_sistema(); #ALMACENARLO EN UNA VARIABLE 
    #OTRA FUNCIONALIDAD
    resultado_juego = self.realizar_diagnostico_sistema_juego()
    resultado_diagnostico["resultados juegos"] = resultado_juego
    return resultado_diagnostico
    
  def realizar_diagnostico_sistema_juego(self):
    juegos= ["FORNITE","COD","GTA"]
    resultados = {}
    for juego in juegos: #JUEGO ME MUESTRA ES EL NOMBRE 
      fps_base = 30
      if "RTX" in self.tarjeta_grafica:
        fps= fps_base*3
      elif "GTX" in self.tarjeta_grafica:
        fps= fps_base*2
      else:
        fps= fps_base
      resultados[juego] = f"{fps} FPS"
    return resultados

  def realizar_informe_uso(self):
      informe=super().realizar_informe_uso()
      informe.update({
         "Tipo": "Gaming",
         "Uso recomendado": "juegos de video",
         "hora de uso": 5,
         "Recomendacion de software" :["antivirus","vpn"]
      })
      return informe 
  pass