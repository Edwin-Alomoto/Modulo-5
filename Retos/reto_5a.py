nombre_paciente = []
edad=[]
ano_actual=2024
def agregar_nombre(nombre,apellido):
  nombre_paciente.append(nombre+" "+apellido)
  

def agregar_edad(ano_nacimento):
  edad_actual= ano_actual-ano_nacimento
  edad.append(edad_actual)

  

def mostrar():
  print(nombre_paciente,edad)
  print("\n")
  edad_min=min(edad)
  edad_max=max(edad)
  posicion1 = edad.index(edad_max)
  print(f"{nombre_paciente[posicion1]} con la edad de {edad_max} años es el mayor a los demas paciente")
  posicion2 = edad.index(edad_min)
  print(f"{nombre_paciente[posicion2]} con la edad de {edad_min} años es el menor a los demas paciente")



 
  
