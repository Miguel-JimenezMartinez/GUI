import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import os
raiz = Tk()

raiz.title("Ventana de pruebas")
raiz.config(bg = "orange")


miframe = Frame(raiz)
miframe.pack(fill="both",expand ="True")
miframe.config(bg = "black")
miframe.config(width = "1280",height = "720")

original = "EJEMPLO.jpg"
anotacion = "EJEMPLO.png"
lista1 = os.listdir(".")
lista2 = os.listdir(".")
direccion1 =('.', '.')
direccion2 =('.', '.')
direccion_anotacion=('.')
lineas= os.listdir(".")

i = 0 #Contador de archivos  
x = 0 #Activador de NEXT
num_li=0
com = 0
if os.path.exists("Chosen.txt"):
	fichero = open("Chosen.txt","r")
	lineas = fichero.readlines()
	num_li = len(lineas)
	fichero.close()
else:
	fichero = open("Chosen.txt","a")	
	fichero.close()




def abrir_archivo():
	global x,original ,anotacion,i,lista1,lista2,direccion1,direccion2,direccion_anotacion

	x = 1
	archivo_abierto = filedialog.askopenfilename(initialdir = "/",
				title = "Seleccione archivo",filetypes = (("jpeg files","*.jpg"),
				("all files",".")))
	direccion1 = os.path.split(archivo_abierto)
	direccion2 = os.path.split(direccion1[0])
	direccion_anotacion = str(direccion2[0])+"/SegmentationClassPNG"
	lista1 = os.listdir(direccion1[0])
	lista2 = os.listdir(direccion_anotacion)
	for i in range (len(lista1)):
		if lista1[i] == direccion1[1]:
			break

	png  = os.path.splitext(lista2[i]) 

	original = direccion1[0] + "/" +lista1[i]
	anotacion = str(direccion_anotacion) +"/"+ lista2[i]
	



	img = Image.open(original) 
	img = img.resize((320, 240), Image.ANTIALIAS) 
	img = ImageTk.PhotoImage(image=img)
	Imagen1.configure(image=img)
	Imagen1.image = img

	img = Image.open(anotacion)  
	img = img.resize((320, 240), Image.ANTIALIAS) 
	img = ImageTk.PhotoImage(image=img)
	Imagen2.configure(image=img)
	Imagen2.image = img

	img_input = np.array(Image.open(original)) / 255.0
	annot_input = np.array(Image.open(anotacion).convert('RGB')) / 255.0
	blend = img_input * 0.4 + annot_input * 0.6

	blend_img = Image.fromarray(np.uint8(blend*255))

	blend_img = blend_img.resize((320, 240), Image.ANTIALIAS) 
	img3 = ImageTk.PhotoImage(image=blend_img)
	Imagen3.configure(image=img3)
	Imagen3.image = img3


	Texto1.configure(text="Imagen: " + direccion1[1])
	Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))


def Next():
	global x,original,anotacion,i,lista1,lista2,direccion1,direccion_anotacion

	if (x > 0 and i < len(lista1)-1):
		i = i +1
		png  = os.path.splitext(lista2[i]) 
		original = direccion1[0] + "/" +lista1[i]
		anotacion = str(direccion_anotacion) +"/"+ png[0]+".png"

		img = Image.open(original) 
		img = img.resize((320, 240), Image.ANTIALIAS) 
		img = ImageTk.PhotoImage(image=img)
		Imagen1.configure(image=img)
		Imagen1.image = img

		img = Image.open(anotacion) 
		img = img.resize((320, 240), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(image=img)
		Imagen2.configure(image=img)
		Imagen2.image = img

		img_input = np.array(Image.open(original)) / 255.0
		annot_input = np.array(Image.open(anotacion).convert('RGB')) / 255.0
		blend = img_input * 0.4 + annot_input * 0.6

		blend_img = Image.fromarray(np.uint8(blend*255))

		blend_img = blend_img.resize((320, 240), Image.ANTIALIAS)
		img3 = ImageTk.PhotoImage(image=blend_img)
		Imagen3.configure(image=img3)
		Imagen3.image = img3


		Texto1.configure(text="Imagen: " + lista1[i])
		Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))

def chos():
	global num_li,x,lista1,lineas,com
	if (x > 0 ):
		fichero = open("Chosen.txt","r")
		lineas = fichero.readlines()
		num_li = len(lineas)
		fichero.close()
		comparador()
		if(com == 0):
			fichero = open("Chosen.txt","a")
			fichero.write(lista1[i]+"\n")
			fichero.close()

		else:
			messagebox.showinfo(message="Imagen repetida", title="Error")
			com = 0	

		fichero = open("Chosen.txt","r")
		lineas = fichero.readlines()
		num_li = len(lineas)
		fichero.close()
		Texto3.configure(text="Chosen: "+str(num_li))
		Next()
			

def comparador():
	global lineas,com,lista1,i,num_li
	m = 0
	for m in range (num_li):
		mensaje = lineas[m]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			break

	     

img1 = Image.open(original)  
img1 = img1.resize((320, 240), Image.ANTIALIAS) 
img1 = ImageTk.PhotoImage(image=img1)

img2 = Image.open(anotacion) 
img2 = img2.resize((320, 240), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(image=img2)

img_input = np.array(Image.open(original)) / 255.0
annot_input = np.array(Image.open(anotacion).convert('RGB')) / 255.0
blend = img_input * 0.4 + annot_input * 0.6

blend_img = Image.fromarray(np.uint8(blend*255))

blend_img = blend_img.resize((320, 240), Image.ANTIALIAS) 
img3 = ImageTk.PhotoImage(image=blend_img)




Imagen1 = Label(miframe, image=img1)
Imagen1.pack(side="bottom", fill="both", expand="yes")
Imagen1.place(x=100,y=200)



Imagen2 = Label(miframe, image=img2)
Imagen2.pack(side="bottom", fill="both", expand="yes")
Imagen2.place(x=420,y=200)


Imagen3 = Label(miframe, image=img3)
Imagen3.pack(side="bottom", fill="both", expand="yes")
Imagen3.place(x=740,y=200)


Texto1 = Label(miframe, text = "Imagen: " + original,fg="black" , font=(32))
Texto1.place(x=100,y=100)

Texto2 = Label(miframe, text = "ID: " + str(i+1) + " out of "+ str(len(lista1)),fg="black" , font=(32))
Texto2.place(x=500,y=100)

Texto3= Label(miframe, text= "Chosen: "+str(num_li) ,fg="black" , font=(32))
Texto3.place(x=870,y=100)


boton1 = Button(raiz, text ="            Abrir            ", font=(18),fg="black", command=abrir_archivo).place(x=250,y=550)	
Label(miframe, button=boton1,height=50, width = 150)

boton2 = Button(raiz, text ="            Elegir            ", font=(18),fg="red", command=chos).place(x=500,y=550)	
Label(miframe, button=boton2,height=50, width = 150)


boton3 = Button(raiz, text ="            Siguiente            ", font=(18),fg="blue", command = Next).place(x=750,y=550)	
Label(miframe, button=boton3,height=50, width = 150)


raiz.mainloop()
