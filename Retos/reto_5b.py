import reto_5a
cantidad = int(input("ingrese la cantidad que va ingresar: "))
for i in range(cantidad):
    print(f"Paciente numero {i}")
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    ano_nacimeinto = int(input("ingrese de año nacimiento:"))
    reto_5a.agregar_nombre(nombre,apellido)
    reto_5a.agregar_edad(ano_nacimeinto)
print("\n")
reto_5a.mostrar()

    
    
    
    
    
    
    
 