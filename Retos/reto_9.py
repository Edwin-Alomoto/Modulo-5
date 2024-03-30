from reto_8 import Laptop_Business
import tkinter as tk 
import tkinter as ttk # 2 PASO

class App_Bussing:
  # 1 PASO
  #METODO CONTRUCTOR 
  def __init__(self, root) -> None:  
    self.root= root  #ROOT ES PARA INICIALIZAR
    self.bussing = [] #GUARDAR EN UNA LISTA LAS LAPTOP BUSSING
    #TITULO EN LA VENTANA 
    root.title("Ingresar datos")

    #INVOCACION # 2 PASO
    self.setup_ui()


  # 2 PASO CUERPO DE LA INTERFAZ GRAFCICA 
  def setup_ui(self):
    # INPUT iNGRESAR DATOS POR PANTALLA 
    ttk.Label(self.root,text="MARCA").grid(row=0,column=0) # DONDE ESTARA UBICADO EN NUESTRA PANTALLA Y LA POSICION
    self.marca = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS QUE INGRESA EL USUARIO 
    ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="PROCESADOR").grid(row=1,column=0) # DONDE ESTARA UBICADO EN NUESTRA PANTALLA Y LA POSICION
    self.procesador = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS QUE INGRESA EL USUARIO 
    ttk.Entry(self.root, textvariable=self.procesador).grid(row=1,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="MEMORIA").grid(row=2,column=0) # DONDE ESTARA UBICADO EN NUESTRA PANTALLA Y LA POSICION
    self.memoria = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS QUE INGRESA EL USUARIO 
    ttk.Entry(self.root, textvariable=self.memoria).grid(row=2,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="COSTO").grid(row=3,column=0) # DONDE ESTARA UBICADO EN NUESTRA PANTALLA Y LA POSICION
    self.costo = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS QUE INGRESA EL USUARIO 
    ttk.Entry(self.root, textvariable=self.costo).grid(row=3,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="IMPUESTO").grid(row=4,column=0) # DONDE ESTARA UBICADO EN NUESTRA PANTALLA Y LA POSICION
    self.impuesto = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS QUE INGRESA EL USUARIO 
    ttk.Entry(self.root, textvariable=self.impuesto).grid(row=4,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

  # 3 GUARDAR DATOS CREACION BOTON 
    #COMMANDO ES PARA INDICAR QUE VA HACER EN ESTE CASO ES AGREGAR UNA NUEVA LAPTOP INVOCANDO UNA FUNCION 
    ttk.Button(self.root, text="Agregar", command=self.agregar_laptop_bussing).grid(row=5,column=0)

  # 4 MOSTRAR POR PANTALLA 
    #MOSTRAR EN LA VENTANA 
    self.mostrar_laptops_bussing = tk.Text(self.root,height=10,width=50) # MOSTRAR EN MI VENTANA 
    self.mostrar_laptops_bussing.grid(row=6,column=0,columnspan=2) #UBICACION EN PANTALLA 



  # 3 FUNCIONALIDAD DEL BOTON  
  def agregar_laptop_bussing(self):
    #OBTENER LA INFORMACION QUE INGRESO EL USUARIO POR PANTALLA
    nuevo_laptop = Laptop_Business(self.marca.get(),self.procesador.get(),self.memoria.get(),self.costo.get(),self.impuesto.get())
    self.bussing.append(nuevo_laptop)
    # 4 MOSTRAR POR PANTALLA 
    self.mostrar_laptops_bussing.insert(tk.END,nuevo_laptop)
    print(nuevo_laptop) # AGREGAR CON LA VARIABLE DONDE SE GUARDA LA INFORMACION 
    
pass

# 1 PASO
#CONSTRUCCION DE LA VENTANA 
root = tk.Tk()
app = App_Bussing(root)
root.mainloop()