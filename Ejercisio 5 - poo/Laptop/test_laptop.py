from laptop import Laptop
# OBEJETO
# PRIMER EJEMPLO
# laptop_pepito = Laptop("Lenovo","i7",32)
# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())
# print(f"el valor de descuento: {laptop_pepito.valor_descuento(10)}")
# # SEGUNDO EJEMPLO
# laptop_pepito = Laptop("Lenovo","i7",32, costo=700)
# laptop_maria = Laptop("Lenovo","i7",32)
# print(Laptop.comparar_costo(laptop_maria,laptop_pepito))
# # TERCERO EJEMPLO
for numero in range (1,1001): #EL COSTO SE SOBRE ESCRIBE CON ESE FOR 
  asus_laptop = Laptop.asus_laptop(numero)
  print(asus_laptop.__dict__)

