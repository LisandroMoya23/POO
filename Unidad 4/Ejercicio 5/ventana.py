from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from Controlador import ManejadorPelicula

class Ventana(object):
	__ventana: None
	def __init__(self,manejador):
		self.__ventana = Tk()
		self.__ventana.title('Cartelera Cine Max')
		self.__ventana.configure(background='gray87')
		self.frameRigth = Frame()
		self.frameRigth.pack(side=RIGHT, fill=Y)
		self.frameRigth.configure(background='gray87')
		frameRigth = Frame()
		frameRigth.pack(side=LEFT, fill=Y)

		self.scrollbar = ttk.Scrollbar(frameRigth)
		self.scrollbar.pack(side=ttk.RIGHT, fill=ttk.Y)
		self.listbox = ttk.Listbox(frameRigth,foreground='gray35',width=31,height=13,yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.listbox.yview)
		self.listbox.pack(side=ttk.LEFT, fill=ttk.BOTH, padx=10, pady=20)
        
		self.manejador = manejador
		self.peliculas = self.manejador.getPelis() 
		for i in range(len(self.peliculas)):
			print("Titulo: ", self.peliculas[i].getTit())
			text = "{}".format(self.peliculas[i].getTit())
			self.listbox.insert(i,text)
		self.listbox.bind("<Double-Button-1>", self.muestraDatos)
		self.__ventana.mainloop()
		
	def muestraDatos(self,event):
		seleccion = self.listbox.curselection()
		if seleccion:
			i= seleccion[0]
			
			self.titulo = self.peliculas[i].getTit()
			self.resumen = self.peliculas[i].getResu()
			self.fecha = self.peliculas[i].getFecha()
			self.lenguaje = self.peliculas[i].getLen()
			titulo = StringVar()
			fecha_lanzamiento = StringVar()
			lenguaje = StringVar()
			fuente_comic_sans = ("Comic Sans MS", 10)
			titulo.set(self.peliculas[i].getTit())
			fecha_lanzamiento.set('Lanzamiento: '+self.peliculas[i].getFecha())
			lenguaje.set('Lenguaje: '+self.peliculas[i].getLen())
			
			titulo_entry=Entry(self.frameRigth,textvariable=titulo,state='disabled',width=31,font='Helvetica 18 bold',justify='center').grid(row=1,column=1,padx=20,pady=15)
			fecha_entry=Entry(self.frameRigth,textvariable=fecha_lanzamiento,state='disabled',font=fuente_comic_sans,width=20,justify='center').grid(row=1,column=0,padx=20,pady=15)
			lenguaje_entry=Entry(self.frameRigth,textvariable=lenguaje,state='disabled',font=fuente_comic_sans,width=20,justify='center').grid(row=1,column=2,padx=20,pady=15)
			resumen_text=Text(self.frameRigth,width=80,height=7)
			resumen_text.grid(row=2,column=0,columnspan=3,pady=20)
			resumen_text.insert(ttk.END,self.peliculas[i].getResu())
			resumen_text.config(state='disabled',font=('Comic Sans MS', 10),foreground='gray35')
		pass

if __name__ == '__main__':
    manejador1 = ManejadorPelicula()
    manejador1.cargaPeli()
    mi_app = Ventana(manejador1)