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
n = 0 #Indicador de Lista DE LA IMAGEN [1 - "NO_ASIGNADO", 2 - "PERFECTO",3 - "MANO", 3 - "PAINT", 4 - "AMBAS_MANOS"]
l = 0 #Indicador de lista SELECCIONADO (BOTON)  [1 - "NO_ASIGNADO", 2 - "PERFECTO","MANO", 3 - "PAINT", 4 - "AMBAS_MANOS"]
kk= 0 #Numero de imagen dentro de lista (PARA MODIFICAR)
num_li_1=0
num_li_2=0
num_li_3=0
num_li_4=0
archivo_abierto = "ruta"


com = 0
nombre_archivo_1 = 'Chosen.txt'
nombre_archivo_2 = 'MANITA.txt'
nombre_archivo_3 = 'PEINT.txt'
nombre_archivo_4 = "Manos"
nombre_archivos = [nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4]
numero_listas = [num_li_1,num_li_2,num_li_3,num_li_4]
nombre_listas = ["NO_ASIGNADO","PERFECTO","MANO", "PAINT", "AMBAS_MANOS"]

def abrir_archivo():
	global x,original,anotacion,nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,nombre_archivos
	global i,lista1,lista2,direccion1,direccion2,direccion_anotacion,n,lineas_1,lineas_2,lineas_3,lineas_4,archivo_abierto
	
	archivo_abierto = filedialog.askopenfilename(initialdir = "./",
				title = "Seleccione archivo",filetypes = (("jpeg files","*.jpg"),
				("all files",".")))
	#print ("archivo abierto: " + archivo_abierto)
	if(1):
		x = 1
		direccion1 = os.path.split(archivo_abierto)
		direccion2 = os.path.split(direccion1[0])
		direccion_anotacion = str(direccion1[0])+"_mask"
		raiz.title(str(direccion1[0]))
		lista1 = os.listdir(direccion1[0])
		lista2 = os.listdir(direccion_anotacion)
		for i in range (len(lista1)):
			if lista1[i] == direccion1[1]:
				break
	
		png  = os.path.splitext(lista2[i]) 
	
		original = direccion1[0] + "/" +lista1[i]
		anotacion = str(direccion_anotacion) +"/"+ lista2[i]
	
		nombre_archivo_1 = direccion2[0] + '/PERFECTO_' + direccion2[1] + '.txt'
		nombre_archivo_2 = direccion2[0] + '/MANO_' + direccion2[1] + '.txt'
		nombre_archivo_3 = direccion2[0] + '/PAINT_' + direccion2[1] + '.txt'
		nombre_archivo_4 = direccion2[0] + '/AMBAS_MANOS_' + direccion2[1] + '.txt'
		nombre_archivos = [nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4]
		if os.path.exists(nombre_archivo_1):
			fichero = open(nombre_archivo_1,"r")
			lineas_1 = fichero.readlines()
			numero_listas[0] = len(lineas_1)
			fichero.close()
		else:
			fichero = open(nombre_archivo_1,"a")	
			fichero.close()
	
		if os.path.exists(nombre_archivo_2):
			fichero = open(nombre_archivo_2,"r")
			lineas_2 = fichero.readlines()
			numero_listas[1] = len(lineas_2)
			fichero.close()
		else:
			fichero = open(nombre_archivo_2,"a")	
			fichero.close()
	
		
		if os.path.exists(nombre_archivo_3):
			fichero = open(nombre_archivo_3,"r")
			lineas_3 = fichero.readlines()
			numero_listas[2] = len(lineas_3)
			fichero.close()
		else:
			fichero = open(nombre_archivo_3,"a")	
			fichero.close()
	
		if os.path.exists(nombre_archivo_4):
			fichero = open(nombre_archivo_4,"r")
			lineas_4 = fichero.readlines()
			numero_listas[3] = len(lineas_4)
			fichero.close()
		else:
			fichero = open(nombre_archivo_4,"a")	
			fichero.close()	
	
		comparador()
	
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
		archivo_abierto = "ruta"
		Imagen3.configure(image=img3)
		Imagen3.image = img3
	
	
		Texto1.configure(text="Imagen: " + direccion1[1])
		Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))
		Texto2_22.configure(text = "Posicion " + nombre_listas[n])
	
		Texto3.configure(text="PERFECTO: "+str(numero_listas[0]))
		Texto4.configure(text="PAINT: "+str(numero_listas[2]))
		Texto5.configure(text="MANO: "+str(numero_listas[1]))
		Texto7.configure(text="AMBAS MANOS: "+str(numero_listas[3]))
	
		Texto6.configure(text="TOTAL: "+str(numero_listas[0] + numero_listas[1] + numero_listas[2]+numero_listas[3]))
	


def Next():
	global x,original,anotacion,i,lista1,lista2,direccion1,direccion_anotacion,n,nombre_archivos, numero_listas

	if (x > 0 and i < len(lista1)-1):
		i = i +1
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
		comparador()
		Texto1.configure(text="Imagen: " + lista1[i])
		Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))
		Texto2_22.configure(text = "Posicion " + nombre_listas[n])

		Texto3.configure(text="PERFECTO: "+str(numero_listas[0]))
		Texto4.configure(text="PAINT: "+str(numero_listas[2]))
		Texto5.configure(text="MANO: "+str(numero_listas[1]))
		Texto7.configure(text="AMBAS MANOS: "+str(numero_listas[3]))	

		Texto6.configure(text="TOTAL: "+str(numero_listas[0] + numero_listas[1] + numero_listas[2]+numero_listas[3]))

	elif(i == len(lista1)-1):
		comparador()
		Texto1.configure(text="Imagen: " + lista1[i])
		Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))
		Texto2_22.configure(text = "Posicion " + nombre_listas[n])

		Texto3.configure(text="PERFECTO: "+str(numero_listas[0]))
		Texto4.configure(text="PAINT: "+str(numero_listas[2]))
		Texto5.configure(text="MANO: "+str(numero_listas[1]))
		Texto7.configure(text="AMBAS MANOS: "+str(numero_listas[3]))	

		Texto6.configure(text="TOTAL: "+str(numero_listas[0] + numero_listas[1] + numero_listas[2]+numero_listas[3]))
		MsgBox = messagebox.askyesnocancel ('Fin de imagenes','Abrir archivos txt      (Sí)\nCerrar programa (No)\nNo hacer nada    (Cancel)',icon = 'warning')
		if (MsgBox == 1):
			abrir()
		elif(MsgBox == 0):
			raiz.destroy()

		



def Last():
	global x,original,anotacion,i,lista1,lista2,direccion1,direccion_anotacion,n,nombre_archivos,numero_listas

	if (x > 0 and i > 0):
		i = i - 1
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
		comparador()	
		Texto1.configure(text="Imagen: " + lista1[i])
		Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))
		Texto2_22.configure(text = "Posicion " + nombre_listas[n])

		Texto3.configure(text="PERFECTO: "+str(numero_listas[0]))
		Texto4.configure(text="PAINT: "+str(numero_listas[2]))
		Texto5.configure(text="MANO: "+str(numero_listas[1]))
		Texto7.configure(text="AMBAS MANOS: "+str(numero_listas[3]))	

		Texto6.configure(text="TOTAL: "+str(numero_listas[0] + numero_listas[1] + numero_listas[2]+numero_listas[3]))
	elif(i == 0 and x > 0):
		MsgBox = messagebox.showinfo(message="Inicio de Imagenes", title="ERROR")









def chos():
	global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,x,lista1,lineas,lineas_1,lineas_2,lineas_3,lineas_4,com,n,l,kk,nombre_archivos, numero_listas
	l=1
	if (x > 0 ):

		comparador()
		if(com == 0):
			fichero = open(nombre_archivo_1,"a")
			fichero.write(lista1[i]+"\n")
			fichero.close()
		else:
			if(n == l):
				messagebox.showinfo(message="La imagen ya se encuentra en esta Lista (" + nombre_listas[n]+")", title="Error")
			else:
				MsgBox = messagebox.askokcancel(title="Error Imagen repetida", message="Desea cambiar la imagen de " +nombre_listas[n] + " a " + nombre_listas[l])
				if (MsgBox == 1):
					fichero = open(nombre_archivos[n-1],"r")
					lines = fichero.readlines()
					fichero.close()
					fichero = open(nombre_archivos[n-1],"w")
					line=0
					for line in range (len(lines)):
						print("line: " + str(line) + "\n kk: "+ str(kk))
						if(line != kk):
							fichero.write(lines[line])
					fichero.close()				
					fichero = open(nombre_archivos[l-1],"a")
					fichero.write(lista1[i]+"\n")
					fichero.close()		
				com = 0	

		fichero = open(nombre_archivo_1,"r")
		lineas = fichero.readlines()
		numero_listas[0] = len(lineas)
		fichero.close()
		Next()



def MANO():
	global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,x,lista1,lineas,lineas_1,lineas_2,lineas_3,lineas_4,com,n,l,kk,nombre_archivos, numero_listas
	l=2
	if (x > 0 ):

		comparador()
		if(com == 0):
			fichero = open(nombre_archivo_2,"a")
			fichero.write(lista1[i]+"\n")
			fichero.close()

		else:
			if(n == l):
				messagebox.showinfo(message="La imagen ya se encuentra en esta Lista (" + nombre_listas[n]+")", title="Error")
			else:
				MsgBox = messagebox.askokcancel(title="Error Imagen repetida", message="Desea cambiar la imagen de " +nombre_listas[n] + " a " + nombre_listas[l])
				if (MsgBox == 1):
					fichero = open(nombre_archivos[n-1],"r")
					lines = fichero.readlines()
					fichero.close()
					fichero = open(nombre_archivos[n-1],"w")
					line=0
					for line in range (len(lines)):
						if(line != kk):
							fichero.write(lines[line])
					fichero.close()				
					fichero = open(nombre_archivos[l-1],"a")
					fichero.write(lista1[i]+"\n")
					fichero.close()		
				com = 0	

		fichero = open(nombre_archivo_2,"r")
		lineas = fichero.readlines()
		numero_listas[1] = len(lineas)
		fichero.close()
		Next()		


def PAINT():
	global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,x,lista1,lineas,lineas_1,lineas_2,lineas_3,lineas_4,com,n,l,kk,nombre_archivos, nombre_listas
	l=3
	if (x > 0 ):

		comparador()
		if(com == 0):
			fichero = open(nombre_archivo_3,"a")
			fichero.write(lista1[i]+"\n")
			fichero.close()

		else:
			if(n == l):
				messagebox.showinfo(message="La imagen ya se encuentra en esta Lista (" + nombre_listas[n]+")", title="Error")
			else:
				MsgBox = messagebox.askokcancel(title="Error Imagen repetida", message="Desea cambiar la imagen de " +nombre_listas[n] + " a " + nombre_listas[l])
				if (MsgBox == 1):
					fichero = open(nombre_archivos[n-1],"r")
					lines = fichero.readlines()
					fichero.close()
					fichero = open(nombre_archivos[n-1],"w")
					line=0
					for line in range (len(lines)):
						if(line != kk):
							fichero.write(lines[line])
					fichero.close()				
					fichero = open(nombre_archivos[l-1],"a")
					fichero.write(lista1[i]+"\n")
					fichero.close()		
				com = 0	

		fichero = open(nombre_archivo_3,"r")
		lineas = fichero.readlines()
		numero_listas[2] = len(lineas)
		fichero.close()
		Next()

def manos():
	global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,x,lista1,lineas,lineas_1,lineas_2,lineas_3,lineas_4,com,n,l,kk,nombre_archivos
	l=4
	if (x > 0 ):
		comparador()
		if(com == 0):
			fichero = open(nombre_archivo_4,"a")
			fichero.write(lista1[i]+"\n")
			fichero.close()

		else:
			if(n == l):
				messagebox.showinfo(message="La imagen ya se encuentra en esta Lista (" + nombre_listas[n]+")", title="Error")
			else:
				MsgBox = messagebox.askokcancel(title="Error Imagen repetida", message="Desea cambiar la imagen de " +nombre_listas[n] + " a " + nombre_listas[l])
				if (MsgBox == 1):
					fichero = open(nombre_archivos[n-1],"r")
					lines = fichero.readlines()
					fichero.close()
					fichero = open(nombre_archivos[n-1],"w")
					line=0
					for line in range (len(lines)):
						if(line != kk):
							fichero.write(lines[line])
					fichero.close()				
					fichero = open(nombre_archivos[l-1],"a")
					fichero.write(lista1[i]+"\n")
					fichero.close()		
				com = 0	

		fichero = open(nombre_archivo_4,"r")
		lineas = fichero.readlines()
		num_li_ = len(lineas)
		fichero.close()
		Next()







def comparador():
	global lineas,com,lista1,i,lineas_1,lineas_2,lineas_3,lineas_4,n,kk,nombre_archivos,numero_listas
	m = 0
	n=0

	fichero = open(nombre_archivo_1,"r")
	lineas_1 = fichero.readlines()
	numero_listas[0] = len(lineas_1)
	fichero.close()

	fichero = open(nombre_archivo_2,"r")
	lineas_2 = fichero.readlines()
	numero_listas[1] = len(lineas_2)
	fichero.close()

	fichero = open(nombre_archivo_3,"r")
	lineas_3 = fichero.readlines()
	numero_listas[2] = len(lineas_3)
	fichero.close()

	fichero = open(nombre_archivo_4,"r")
	lineas_4 = fichero.readlines()
	numero_listas[3] = len(lineas_4)
	fichero.close()

	for m in range (numero_listas[0]):
		mensaje = lineas_1[m]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=1
			kk = m
			break
	m = 0		
	for m in range (numero_listas[1]):
		mensaje = lineas_2[m]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=2
			kk = m
			break		
	m = 0		
	for m in range (numero_listas[2]):
		mensaje = lineas_3[m]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=3
			kk = m
			break

	m = 0		
	for m in range (numero_listas[3]):
		mensaje = lineas_4[m]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=4
			kk = m
			break				




def abrir():
    global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3, nombre_archivo_4

    os.startfile(nombre_archivo_1) 
    os.startfile(nombre_archivo_2) 
    os.startfile(nombre_archivo_3)
    os.startfile(nombre_archivo_4)  
	     

def Organizar():
	global x
	if(x>0):
		for x in range(4):
			fichero = open(nombre_archivos[x],"r")
			lines = fichero.readlines()
			lines.sort()
			fichero.close()	
	
			fichero = open(nombre_archivos[x],"w")
			for line in lines:
				fichero.write(line)
	
			fichero.close()
	

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

Texto2_22 = Label(miframe, text = "Posicion: " + nombre_listas[n] ,fg="black" , font=(32))
Texto2_22.place(x=500,y=125)

Texto4= Label(miframe, text= "PAINT: "+str(numero_listas[2]) ,fg="black" , font=(32))
Texto4.place(x=870,y=13)
Texto3= Label(miframe, text= "PERFECTO: "+str(numero_listas[0]) ,fg="black" , font=(32))
Texto3.place(x=870,y=46)
Texto5= Label(miframe, text= "MANO: "+str(numero_listas[1]) ,fg="black" , font=(32))
Texto5.place(x=870,y=115)
Texto6= Label(miframe, text= "TOTAL: "+str(numero_listas[0] + numero_listas[1] + numero_listas[2]+numero_listas[3]) ,fg="black" , font=(32))
Texto6.place(x=870,y=150)
Texto7= Label(miframe, text= "AMBAS MANOS: "+str(numero_listas[3]) ,fg="black" , font=(32))
Texto7.place(x=870,y=80)


boton1 = Button(raiz, text ="          PAINT (Q)        ", font=(18),fg="red", command=PAINT).place(x=30,y=500)	
Label(miframe, button=boton1,height=50, width = 130)

boton2 = Button(raiz, text ="           PERFECTO (W)        ", font=(18),fg="red", command=chos).place(x=275,y=500)	
Label(miframe, button=boton2,height=50, width = 130)

boton2_2 = Button(raiz, text ="          AMBAS MANOS (E)        ", font=(18),fg="red", command=manos).place(x=580,y=500)	
Label(miframe, button=boton2_2,height=50, width = 130)


boton3 = Button(raiz, text ="            MANO (R)        ", font=(18),fg="red", command=MANO).place(x=910,y=500)	
Label(miframe, button=boton3,height=50, width = 130)


boton4 = Button(raiz, text ="            Anterior           ", font=(18),fg="blue", command = Last).place(x=250,y=600)	
Label(miframe, button=boton4,height=50, width = 150)

boton5 = Button(raiz, text ="            Abrir            ", font=(18),fg="black", command=abrir_archivo).place(x=515,y=600)	
Label(miframe, button=boton5,height=50, width = 150)

boton6 = Button(raiz, text ="            Siguiente            ", font=(18),fg="blue", command = Next).place(x=750,y=600)	
Label(miframe, button=boton6,height=50, width = 150)

boton7 = Button(raiz, text ="     ORGANIZAR     ", font=(18),fg="GREEN", command = Organizar).place(x=1050,y=650)
Label(miframe, button=boton6,height=50, width = 150)

def boton_p(event):
	
	bp= event.keysym
	if bp =="Right":
		Next()
	elif bp == "Left":
		Last()
	elif bp == "Q" or bp == "q":
		PAINT()
	elif bp == "W" or bp == "w":
		chos()
	elif bp == "E" or bp == "e":
		manos()
	elif bp == "R" or bp == "r":
		MANO()				




raiz.bind("<Key>", boton_p)



raiz.mainloop()
