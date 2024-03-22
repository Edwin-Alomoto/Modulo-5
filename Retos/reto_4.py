datos=[]
contador_numero=0;
contador_letras=0;
contador_otros=0;
valor=input("ingrese datos: ")
for i in valor:
  ascii= ord(i) #También podemos obtener el valor ASCII de cada carácter de una cadena
  if (ascii>=65 and ascii<=90) or (ascii>=97 and ascii<=122):
    datos.append(i)
    contador_letras+=1
  elif ascii>=48 and ascii<=57:
    datos.append(i)
    contador_numero+=1
  else:
    contador_otros+=1
print("Cantidad de valores string son: ",contador_letras)
print("Cantidad de valores numericos son: ",contador_numero)
print("Cantidad de valores de otros tipo datos que no fueron agregados son: ",contador_otros)
print(f"Su lista es: {datos}")


 
