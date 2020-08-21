import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import os, sys, subprocess
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
direccionm = "0"
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
abrir_e= 0
def abrir_archivo():
	global x,original,anotacion,nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,nombre_archivos,abrir_e
	global i,lista1,lista2,direccion1,direccion2,direccion_anotacion,n,lineas_1,lineas_2,lineas_3,lineas_4,archivo_abierto,direccionm,n
	abrir_e=1
	print(str(abrir_e))
	archivo_abierto = filedialog.askopenfilename(initialdir = "./",
				title = "Seleccione archivo",filetypes = (("jpeg files","*.jpg"),
				("all files",".")))
	#print ("archivo abierto: " + archivo_abierto)
	print(archivo_abierto)
	

	if(len(archivo_abierto) != 0):
		x = 1
		direccion1 = os.path.split(archivo_abierto)
		direccion2 = os.path.split(direccion1[0])
		direccion_anotacion = str(direccion1[0])+"_mask"
		raiz.title(str(direccion1[0]))
		lista1 = os.listdir(direccion1[0])	
		try:
			os.stat(direccion2[0] + "/Listas")
		except OSError as e:
			os.mkdir(direccion2[0] + "/Listas")		

		lista2 = os.listdir(direccion_anotacion)
		lista1.sort()
		lista2.sort()
		print(lista1)

		for i in range (len(lista1)):
			if lista1[i] == direccion1[1]:
				break
	
		png  = os.path.splitext(lista2[i]) 
	
		original = direccion1[0] + "/" +lista1[i]
		anotacion = str(direccion_anotacion) +"/"+ lista2[i]
	
		nombre_archivo_1 = direccion2[0] + "/Listas" + '/PERFECTO_' + direccion2[1] + '.txt'
		nombre_archivo_2 = direccion2[0] + "/Listas" + '/MANO_' + direccion2[1] + '.txt'
		nombre_archivo_3 = direccion2[0] + "/Listas" + '/PAINT_' + direccion2[1] + '.txt'
		nombre_archivo_4 = direccion2[0] + "/Listas" + '/AMBAS_MANOS_' + direccion2[1] + '.txt'
		nombre_archivos = [nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4]
		if os.path.exists(nombre_archivo_1):
			fichero = open(nombre_archivo_1,"r")
			lineas_1 = fichero.readlines()
			fichero.close()
			if(len(lineas_1) != 0):
				if((direccion2[1] + "\n" != lineas_1[0])):
					lineas_1.insert(0,direccion2[1]+"\n")
					fichero = open(nombre_archivo_1,"w")	
					for c in lineas_1:
						fichero.write(c)
					fichero.close()
			else:
				fichero = open(nombre_archivo_1,"a+")	
				fichero.write(direccion2[1] + "\n")
				fichero.close()	
			
			
		else:
			fichero = open(nombre_archivo_1,"a+")	
			fichero.write(direccion2[1] + "\n")
			fichero.close()
	
		if os.path.exists(nombre_archivo_2):
			fichero = open(nombre_archivo_2,"r")
			lineas_2 = fichero.readlines()
			fichero.close()

			if(len(lineas_2) != 0):
				if((direccion2[1] + "\n" != lineas_2[0])):
					lineas_2.insert(0,direccion2[1]+"\n")
					fichero = open(nombre_archivo_2,"w")	
					for c in lineas_2:
						fichero.write(c)
					fichero.close()
			else:
				fichero = open(nombre_archivo_2,"a+")	
				fichero.write(direccion2[1] + "\n")
				fichero.close()	
			
		else:
			fichero = open(nombre_archivo_2,"a+")	
			fichero.write(direccion2[1] + "\n")
			fichero.close()
	
		
		if os.path.exists(nombre_archivo_3):
			fichero = open(nombre_archivo_3,"r")
			lineas_3 = fichero.readlines()
			fichero.close()
			
			if(len(lineas_3) != 0):
				if((direccion2[1] + "\n" != lineas_3[0])):
					lineas_3.insert(0,direccion2[1]+"\n")
					fichero = open(nombre_archivo_3,"w")	
					for c in lineas_3:
						fichero.write(c)
					fichero.close()
			else:
				fichero = open(nombre_archivo_3,"a+")	
				fichero.write(direccion2[1] + "\n")
				fichero.close()	

			
		else:
			fichero = open(nombre_archivo_3,"a+")	
			fichero.write(direccion2[1] + "\n")
			fichero.close()
	
		if os.path.exists(nombre_archivo_4):
			fichero = open(nombre_archivo_4,"r")
			lineas_4 = fichero.readlines()
			fichero.close()

			if(len(lineas_4) != 0):
				if((direccion2[1] + "\n" != lineas_4[0])):
					lineas_4.insert(0,direccion2[1]+"\n")
					fichero = open(nombre_archivo_4,"w")	
					for c in lineas_4:
						fichero.write(c)
					fichero.close()
			else:
				fichero = open(nombre_archivo_4,"a+")	
				fichero.write(direccion2[1] + "\n")
				fichero.close()	

		else:
			fichero = open(nombre_archivo_4,"a+")	
			fichero.write(direccion2[1] + "\n")
				
	
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
	
	
		Texto1.configure(text="Imagen: " + lista1[0])
		Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))
		Texto2_22.configure(text = "Posicion " + nombre_listas[n])
	
		Texto3.configure(text="PERFECTO: "+str(numero_listas[0]))
		Texto4.configure(text="PAINT: "+str(numero_listas[2]))
		Texto5.configure(text="MANO: "+str(numero_listas[1]))
		Texto7.configure(text="AMBAS MANOS: "+str(numero_listas[3]))
	
		Texto6.configure(text="TOTAL: "+str(numero_listas[0] + numero_listas[1] + numero_listas[2]+numero_listas[3]))

def abrir_archivo_2():
	global x,original,anotacion,nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,nombre_archivos,abrir_e,n
	global i,lista1,lista2,direccion1,direccion2,direccion_anotacion,n,lineas_1,lineas_2,lineas_3,lineas_4,archivo_abierto,direccionm
	abrir_e=2
	archivo_abierto = filedialog.askopenfilename(initialdir = "./",
				title = "Seleccione archivo",filetypes = (("Listas","*.txt"),
				("all files",".")))
	#print ("archivo abierto: " + archivo_abierto)
	
	print(archivo_abierto)
	if(len(archivo_abierto) != 0):
		fichero = open(archivo_abierto,"r")
		lineas = fichero.readlines()
		numero = len(lineas)
		fichero.close()

		for x in range (numero ):
			lineas[x] = lineas[x][0:(len(lineas[x]) - 1)]
			m = os.path.splitext(lineas[x])
			lineas[x] = m[0]
	 
		png  = os.path.splitext(lista2[i]) 	

		#print(lineas)
		#print(" , ")
		#print(str(numero))
		if(numero > 1):
			x = 1
			i=0
			direccion1 = os.path.split(archivo_abierto)
			direccionm = direccion1[1][(len(direccion1[1]) - 7):(len(direccion1[1]) - 4)] #po1,po2,rg1,rg2
			#print("Aqui: " +direccionm)
			direccion2 = os.path.split(direccion1[0]) 
			direccion_anotacion = str(direccion1[0])+"_mask"
			raiz.title(str(direccion1[0]))
			#lista1 = os.listdir(direccion1[0])
			lista1 = lineas[1:len(lineas)]
			lista2 = lineas
			try:
				
				os.stat(direccion2[0] + "/Revision")
			except OSError as e:
				os.mkdir(direccion2[0] + "/Revision")

			"""
			for i in range (len(lista1)):
				if lista1[i] == direccion1[1]:
					break
			
			png  = os.path.splitext(lista2[i]) 
			"""
			original = direccion2[0]+ "/" +direccionm + "/" +lista1[i] +".jpg"
			anotacion = direccion2[0]+ "/" +direccionm +"_mask" + "/" +lista1[i] +".png"
		
			nombre_archivo_1 = direccion2[0] + "/Revision" + '/PERFECTO_' + direccionm + "_rev" + '.txt'
			nombre_archivo_2 = direccion2[0] + "/Revision" + '/MANO_' + direccionm + "_rev" + '.txt'
			nombre_archivo_3 = direccion2[0] + "/Revision" + '/PAINT_' + direccionm + "_rev" + '.txt'
			nombre_archivo_4 = direccion2[0] + "/Revision" + '/AMBAS_MANOS_' + direccionm + "_rev" + '.txt'
			nombre_archivos = [nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4]
			if os.path.exists(nombre_archivo_1):
				fichero = open(nombre_archivo_1,"r")
				lineas_1 = fichero.readlines()
				fichero.close() 
				if(len(lineas_1) != 0):
					numero_listas[0] = len(lineas_1)
					if((direccionm + "\n" != lineas_1[0])):
						lineas_1.insert(0,direccionm+"\n")
						fichero = open(nombre_archivo_1,"w")	
						for c in lineas_1:
							fichero.write(c)
						fichero.close()
				else: 	
					fichero = open(nombre_archivo_1,"a+")	
					fichero.write(direccionm + "\n")
					fichero.close()
					numero_listas[0] = 0
			else:
				fichero = open(nombre_archivo_1,"a+")	
				fichero.write(direccionm + "\n")
				fichero.close()
				numero_listas[0] = 0
		
			if os.path.exists(nombre_archivo_2):
				fichero = open(nombre_archivo_2,"r")
				lineas_2 = fichero.readlines()
				fichero.close()	

				if(len(lineas_2) != 0):
					numero_listas[1] = len(lineas_2)
					if((direccionm + "\n" != lineas_2[0])):
						lineas_2.insert(0,direccionm+"\n")
						fichero = open(nombre_archivo_2,"w")	
						for c in lineas_2:
							fichero.write(c)
						fichero.close()
				else: 	
					fichero = open(nombre_archivo_2,"a+")	
					fichero.write(direccionm + "\n")
					fichero.close()
					numero_listas[1] = 0
			else:
				fichero = open(nombre_archivo_2,"a")	
				fichero.write(direccionm + "\n")
				fichero.close()
		
			
			if os.path.exists(nombre_archivo_3):
				fichero = open(nombre_archivo_3,"r")
				lineas_3 = fichero.readlines()
				fichero.close()
				if(len(lineas_3) != 0):
					numero_listas[2] = len(lineas_3)
					if((direccionm + "\n" != lineas_3[0])):
						lineas_3.insert(0,direccionm+"\n")
						fichero = open(nombre_archivo_3,"w")	
						for c in lineas_3:
							fichero.write(c)
						fichero.close()
				else: 	
					fichero = open(nombre_archivo_3,"a+")	
					fichero.write(direccionm + "\n")
					fichero.close()
					numero_listas[2] = 0
				
			else:
				fichero = open(nombre_archivo_3,"a")	
				fichero.write(direccionm + "\n")
				fichero.close()
		
			if os.path.exists(nombre_archivo_4):
				fichero = open(nombre_archivo_4,"r")
				lineas_4 = fichero.readlines()
				fichero.close()
				if(len(lineas_4) != 0):
					numero_listas[3] = len(lineas_4)
					if((direccionm + "\n" != lineas_4[0])):
						lineas_4.insert(0,direccionm+"\n")
						fichero = open(nombre_archivo_4,"w")	
						for c in lineas_4:
							fichero.write(c)
						fichero.close()
				else: 	
					fichero = open(nombre_archivo_4,"a+")	
					fichero.write(direccionm + "\n")
					fichero.close()
					numero_listas[3] = 0

			else:
				fichero = open(nombre_archivo_4,"a")	
				fichero.write(direccionm + "\n")
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
		
		
			Texto1.configure(text="Imagen: " + lista1[0])
			Texto2.configure(text= "ID: " + str(i+1) + " out of "+ str(len(lista1)))
			Texto2_22.configure(text = "Posicion " + nombre_listas[n])
		
			Texto3.configure(text="PERFECTO: "+str(numero_listas[0]))
			Texto4.configure(text="PAINT: "+str(numero_listas[2]))
			Texto5.configure(text="MANO: "+str(numero_listas[1]))
			Texto7.configure(text="AMBAS MANOS: "+str(numero_listas[3]))
		
			Texto6.configure(text="TOTAL: "+str(numero_listas[0] + numero_listas[1] + numero_listas[2]+numero_listas[3]))		
		else:
			MsgBox = messagebox.showinfo(message="La lista esta vacia", title="ERROR")


def Next():
	global x,original,anotacion,i,lista1,lista2,direccion1,direccion_anotacion,n,nombre_archivos, numero_listas,direccionm
	global abrir_e
	if (x > 0 and i < len(lista1)-1):
		i = i +1
		if(abrir_e ==2):
			original = direccion2[0]+ "/" +direccionm + "/" +lista1[i] +".jpg"
			anotacion = direccion2[0]+ "/" +direccionm +"_mask" + "/" +lista1[i] +".png"
		elif(abrir_e == 1):	
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
	global x,original,anotacion,i,lista1,lista2,direccion1,direccion_anotacion,n,nombre_archivos,numero_listas,direccionm
	global abrir_e
	if (x > 0 and i > 0):
		i = i - 1

		if(abrir_e ==2):
			original = direccion2[0]+ "/" +direccionm + "/" +lista1[i] +".jpg"
			anotacion = direccion2[0]+ "/" +direccionm +"_mask" + "/" +lista1[i] +".png"
		elif(abrir_e == 1):	
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
			fichero = open(nombre_archivos[l-1],"a")
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
						#print("line: " + str(line) + "\n kk: "+ str(kk))
						if(line != kk):
							fichero.write(lines[line])
					fichero.close()				
					fichero = open(nombre_archivos[l-1],"a")
					fichero.write(lista1[i]+"\n")
					fichero.close()		
				com = 0	

		fichero = open(nombre_archivo_1,"r")
		lineas = fichero.readlines()
		numero_listas[0] = len(lineas)  - 1
		fichero.close()
		Next()



def MANO():
	global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,x,lista1,lineas,lineas_1,lineas_2,lineas_3,lineas_4,com,n,l,kk,nombre_archivos, numero_listas
	l=2
	if (x > 0 ):

		comparador()
		if(com == 0):
			fichero = open(nombre_archivos[l-1],"a")
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
		print(str(com))
		if(com == 0):
			fichero = open(nombre_archivos[l-1],"a")
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
		numero_listas[2] = len(lineas)  - 1
		fichero.close()
		Next()



def manos():
	global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,x,lista1,lineas,lineas_1,lineas_2,lineas_3,lineas_4,com,n,l,kk,nombre_archivos
	l=4
	if (x > 0 ):
		comparador()
		if(com == 0):
			fichero = open(nombre_archivos[l-1],"a")
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


def BORRAR():
	global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3,nombre_archivo_4,x,lista1,lineas,lineas_1,lineas_2,lineas_3,lineas_4,com,n,l,kk,nombre_archivos, numero_listas
	l=1
	if (x > 0 ):

		comparador()
		if(com == 0):
			messagebox.showinfo(message="La imagen NO se encuentra en ninguna lista ", title="Error")
		else:
			MsgBox = messagebox.askokcancel(title="Error Imagen repetida", message="Desea eliminar la imagen de " + nombre_listas[n])
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
				#fichero = open(nombre_archivos[l-1],"a")
				#fichero.write(lista1[i]+"\n")
				#fichero.close()		
			com = 0	

		fichero = open(nombre_archivo_1,"r")
		lineas = fichero.readlines()
		numero_listas[0] = len(lineas) - 1
		fichero.close()
		Next()




def comparador():
	global lineas,com,lista1,i,lineas_1,lineas_2,lineas_3,lineas_4,n,kk,nombre_archivos,numero_listas
	m = 0
	n=0
	com =0
	fichero = open(nombre_archivo_1,"r")
	lineas_1 = fichero.readlines()
	numero_listas[0] = len(lineas_1) - 1
	fichero.close()

	fichero = open(nombre_archivo_2,"r")
	lineas_2 = fichero.readlines()
	numero_listas[1] = len(lineas_2) - 1
	fichero.close()

	fichero = open(nombre_archivo_3,"r")
	lineas_3 = fichero.readlines()
	numero_listas[2] = len(lineas_3) - 1
	fichero.close()

	fichero = open(nombre_archivo_4,"r")
	lineas_4 = fichero.readlines()
	numero_listas[3] = len(lineas_4) - 1
	fichero.close()

	for m in range (numero_listas[0]):
		mensaje = lineas_1[m + 1]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=1
			kk = m + 1
			break
	m = 0		
	for m in range (numero_listas[1]):
		mensaje = lineas_2[m + 1]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=2
			kk = m + 1
			break		
	m = 0		
	for m in range (numero_listas[2]):
		mensaje = lineas_3[m + 1]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=3
			kk = m + 1
			break

	m = 0		
	for m in range (numero_listas[3]):
		mensaje = lineas_4[m + 1]
		mensaje = mensaje[0:len(mensaje)-1]
		#print("Esto es m" + str(m))
		#print("Linea " + str(m+1) +" contiene " + lineas[m] + "---- comparado con " + lista1[i])
		if mensaje == lista1[i]:
			com = 1
			n=4
			kk = m + 1
			break				




def abrir():
    global nombre_archivo_1,nombre_archivo_2,nombre_archivo_3, nombre_archivo_4
    open_file(nombre_archivo_1) 
    open_file(nombre_archivo_2) 
    open_file(nombre_archivo_3)
    open_file(nombre_archivo_4)  
	     
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
	     

def Organizar():
	global x
	if(x>0):
		for x in range(4):
			fichero = open(nombre_archivos[x],"r")
			lines = fichero.readlines()
			
			fichero.close()	
			
			fichero = open(nombre_archivos[x],"w")
			fichero.write(lines[0])
			lines.sort()
			M =(len(lines) -1)
			lines_2 = lines[0:M]
			
			for line in range (len(lines_2)):
				fichero.write(lines_2[line])
	
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


boton1 = Button(raiz, text ="          PAINT (Q)        ", font=(18),fg="red", command=PAINT).place(x=75,y=500)	
Label(miframe, button=boton1,height=50, width = 130)

boton2 = Button(raiz, text ="           PERFECTO (W)        ", font=(18),fg="red", command=chos).place(x=275,y=500)	
Label(miframe, button=boton2,height=50, width = 130)

boton2_2 = Button(raiz, text ="          AMBAS MANOS (E)        ", font=(18),fg="red", command=manos).place(x=525,y=500)	
Label(miframe, button=boton2_2,height=50, width = 130)

boton3 = Button(raiz, text ="            MANO (R)        ", font=(18),fg="red", command=MANO).place(x=800,y=500)	
Label(miframe, button=boton3,height=50, width = 130)

boton7_2 = Button(raiz, text ="     BORRAR (B)    ", font=(18),fg="RED", command = BORRAR).place(x=1020,y=500)
Label(miframe, button=boton7_2,height=50, width = 150)

boton4 = Button(raiz, text ="            Anterior           ", font=(18),fg="blue", command = Last).place(x=250,y=600)	
Label(miframe, button=boton4,height=50, width = 150)

boton5 = Button(raiz, text ="            Abrir (Imagenes)   ", font=(18),fg="black", command=abrir_archivo).place(x=515,y=600)	
Label(miframe, button=boton5,height=50, width = 150)

boton5_2 = Button(raiz, text ="            Abrir (TXT'S)        ", font=(18),fg="black", command=abrir_archivo_2).place(x=515,y=650)	
Label(miframe, button=boton5_2,height=50, width = 150)

boton6 = Button(raiz, text ="            Siguiente            ", font=(18),fg="blue", command = Next).place(x=800,y=600)	
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
	elif bp == "B" or bp == "b":	
		BORRAR()




raiz.bind("<Key>", boton_p)



raiz.mainloop()
#