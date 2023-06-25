from tkinter import *
from tkinter import  ttk, messagebox
class Ventana(object):
	__ventana = None
	def __init__(self):
		self.__ventana = Tk()
		self.__ventana.title('Calculadora IPC')
		self.__ventana.configure(background='gray87')
		self.mainframe = Frame()
		self.mainframe.pack()
		self.mainframe.configure(background='gray87')
		self.seleccion=BooleanVar()
		ttk.Label(self.mainframe, text="Calculo IVA").grid(column=0, row=0)
		ttk.Label(self.mainframe, text="Precio sin iva:").grid(column=0, row=2, sticky=W)
		ttk.Label(self.mainframe, text="IVA").grid(column=0, row=5, padx=10, sticky=W)
		ttk.Label(self.mainframe, text='', width=10, background='white').grid(column=1, row=5)
		ttk.Label(self.mainframe, text="Precio con IVA:").grid(column=0, row=6, padx=10)
		ttk.Label(self.mainframe, text='', width=10, background='white').grid(column=1, row=6)

		self.botonframe=Frame()
		self.botonframe.pack()
		self.botonframe.configure(bg='gray83')
		ttk.Button(self.botonframe, text='Calcular', command=self.calcular).grid(column=0, row=7, sticky=W, padx=25, pady=10)
		ttk.Button(self.botonframe, text='Salir', command=self.__ventana.destroy).grid(column=1, row=7, sticky=W, padx=25, pady=10)
		ttk.Radiobutton(self.mainframe, text='IVA 21%', value=0, variable=self.seleccion).grid(column=0, row=3,columnspan=1,sticky='w')
		ttk.Radiobutton(self.mainframe, text='IVA 10.5%', value=1, variable=self.seleccion).grid(column=0, row=4,columnspan=1,sticky='w')

		self.precioSin=Entry(self.mainframe, width=10)
		self.precioSin.grid(column=1, row=2, sticky=W, padx=0, pady=0)
		self.__ventana.mainloop()

	def calcular(self):
		try:
			if self.seleccion.get() == 0:
				precioIVA= float(self.precioSin.get()) *(21/100)
				precioConIVa = float(self.precioSin.get()) + precioIVA
			elif self.seleccion.get() == 1:
				precioIVA= float(self.precioSin.get()) *(10.5/100)
				precioConIVa = float(self.precioSin.get()) + precioIVA
			Label(self.mainframe, text=precioIVA).grid(column=1, row=5, sticky=W)
			Label(self.mainframe, text=precioConIVa).grid(column=1, row=6, sticky=W)
		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor numerico.')

if __name__ == '__main__':
	mi_app = Ventana()