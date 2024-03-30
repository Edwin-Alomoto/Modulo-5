from laptop_gaming import Laptop_Gaming
import tkinter as tk #CONSTRUCCION DE LA INTERFAZ GRAFICO 
from tkinter import ttk #WIDGET QUE VA ESTAR 
from PIL import Image, ImageTk #PARA LA IMAGENES
import random

#CONTRUCCION DE LA CLASE
class App:
  #METODO CONTRCTOR 
  # ROOT ES PARA INICIALIZAR
  def __init__(self, root) -> None:
    self.root = root
    #GUARDAR EN UNA LISTA LAS LAPTOP GAMMING 
    self.laptops = []
    self.imagenes =["C:\\Users\\Pc\\Documents\\Programacion\\Modulo 5\\Ejercisio 5 - poo\\Laptop\\img\1.jpg","C:\\Users\\Pc\\Documents\\Programacion\\Modulo 5\\Ejercisio 5 - poo\\Laptop\\img\\2.jpg","C:\\Users\\Pc\\Documents\\Programacion\\Modulo 5\\Ejercisio 5 - poo\\Laptop\\img\\3.jpg","C:\\Users\\Pc\\Documents\\Programacion\\Modulo 5\\Ejercisio 5 - poo\\Laptop\\img\\4.jpg","C:\\Users\\Pc\\Documents\\Programacion\\Modulo 5\\Ejercisio 5 - poo\\Laptop\\img\\5.jpg"]
    #TITULO EN LA VENTANA 
    root.title("Ingresar datos")
    #CREAR UN METODO
    self.setup_ui()
  
  def setup_ui(self):
    # INPUT 
    ttk.Label(self.root,text="MARCA").grid(row=0,column=0) #UBICADA EN NUESTRA PANTALLA Y LA POSICION
    self.marca = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS AL USUARIO 
    ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="PROCESADOR").grid(row=1,column=0) #UBICADA EN NUESTRA PANTALLA Y LA POSICION
    self.procesador = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS AL USUARIO 
    ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="MEMORIA").grid(row=2,column=0) #UBICADA EN NUESTRA PANTALLA Y LA POSICION
    self.memoria = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS AL USUARIO 
    ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="TARJETA GRAFICA").grid(row=3,column=0) #UBICADA EN NUESTRA PANTALLA Y LA POSICION
    self.tarjeta = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS AL USUARIO 
    ttk.Entry(self.root,textvariable=self.tarjeta).grid(row=3,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA

    ttk.Label(self.root,text="PRECIO").grid(row=4,column=0) #UBICADA EN NUESTRA PANTALLA Y LA POSICION
    self.precio = tk.StringVar() #INGRESAR UN INPUT # LIBRERIA PARA EL MANEJO DE DATOS AL USUARIO 
    ttk.Entry(self.root,textvariable=self.precio).grid(row=4,column=1)#DONDE VA ALMACENADO EL VALOR QUE SE INGRESA
    #BOTON 
    ttk.Button(self.root,text="Agregar Laptop", command=self.agregar_laptop).grid(row=5,column=0)#COMMANDO ES PARA INDICAR QUE VA HACER EN ESTE CASO ES AGREGAR UNA NUEVA LAPTOP INVOCANDO UNA FUNCION 
    #MOSTRAR EN LA VENTANA 
    self.mostrar_laptops = tk.Text(self.root,height=10,width=50) # MOSTRAR EN MI VENTANA 
    self.mostrar_laptops.grid(row=6,column=0,columnspan=2) #UBICACION EN PANTALLA 
    
    #COLOCACION DE IMAGENES 
    self.canva = tk.Canvas(self.root,width=200,height=200) #MOSTRAR EN PANTALLA 
    self.canva.grid(row=1,column=3,rowspan=6) #UBICACION EN PANTALLA

  #FUNCIONALIDAD DEL BOTON 
  def agregar_laptop(self):
      nuevo_laptop = Laptop_Gaming(self.marca.get(),self.procesador.get(),self.memoria.get(),self.tarjeta.get(),self.precio.get())
      self.laptops.append(nuevo_laptop)
      self.mostrar_laptops.insert(tk.END,nuevo_laptop)
      print(self.laptops[0])
      #MOSTRAR IMAGEN INVOCACION DE LA FUNCION 
      self.mostrar_imagen_aletorias()
  #FUNCIONALIDAD PARA COLOCAR LA IMGEN 
  def mostrar_imagen_aletorias(self):
     imagen_path= random.choice(self.imagenes)
     imagen = Image.open(imagen_path)#ABRIR LA IMAGEN 
     imagen = imagen.resize((200,200),Image.Resampling.LANCZOS) #REDIMENSIONAR LA IMAGEN 
     photo = ImageTk.PhotoImage(imagen) #DARLE EL FORMATO
     self.canva.create_image(0,0,anchor=tk.NW,image=photo) #COORDENADAS 
     self.canva.image=photo
pass

#VENTANA CONSTRUIDA
root = tk.Tk()
#VISTASO DE LA CONSTRUCCION DE NUESTRA INTERFAZ
app =  App(root)
#ESCUCHAR TODO LOS EVENTOS QUE SUCEDE EN MI VENTANA 
root.mainloop();
