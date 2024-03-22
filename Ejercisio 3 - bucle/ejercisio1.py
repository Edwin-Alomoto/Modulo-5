#BUCLES
lista = [1,2,3,4,5,6,"Anthony","Pedro",1,2,3,4,6,6,"Anthony"]
elemento="Pedro"
#FOR
for i in lista:
  #print(i,end=(",")) #IMPRIME LA LISTA Y ADEMAS LO COLOCA DE MANERA HORIZONTAL CON COMA
  if i==elemento:
    print(f"El elemento {elemento} esta dentro de la lista")

