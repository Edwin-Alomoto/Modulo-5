#UTILIZACION DEL FOR CON EL IF MAS EL CONTADOR 
frase = input("Ingrese una frase: ")
letras = input("ingrese una letra: ")

contador=0 
for i in frase:
  if i==letras:
    contador+=1
print(f"La letra {letras} se repite {contador}")
print(frase.count(letras))