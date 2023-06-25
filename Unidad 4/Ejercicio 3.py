from tkinter import *
from tkinter import  ttk, messagebox
from urllib.request import urlopen
import json

class Ventana(object):
	__ventana = None
	__dolares = None
	def __init__(self):
		self.__ventana = Tk()
		self.__dolares = StringVar()
		self.__ventana.title('Calculadora IPC')
		self.__ventana.configure(background='gray87')
		self.mainframe = Frame()
		self.mainframe.pack()
		self.mainframe.configure(background='gray87')

		self.pesos = Entry(self.mainframe,width=10)
		self.pesos.grid(column=2, row=1, sticky=E, padx=0, pady=0)


		Label(self.mainframe, text='dolares', background='gray87').grid(column=3, row=1, sticky=W)
		Label(self.mainframe, text='Es equivalente a', background='gray87').grid(column=1, row=2, sticky=W)
		Label(self.mainframe, textvariable= self.__dolares, background='gray87').grid(column=2, row=2, sticky=W)
		Label(self.mainframe, text='pesos', background='gray87').grid(column=3, row=2, sticky=W)

		
		ttk.Button(self.mainframe, text='Calcular', command=self.calcular).grid(column=1, row=4, sticky=W)
		ttk.Button(self.mainframe, text='Salir', command=self.__ventana.destroy).grid(column=2, row=4, sticky=W)

		url = "https://www.dolarsi.com/api/api.php?type=dolar"
		response = urlopen(url)
		self.data = json.loads(response.read())
		self.__ventana.mainloop()

	def calcular(self):
		try:
			cotizacion = self.data[0]['casa']['venta']
			cotizacion = cotizacion.replace(',','.')
			dolar = float(self.pesos.get()) * float(cotizacion)
			self.__dolares.set(dolar)
		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor numerico.')
			
if __name__ == '__main__':
	mi_app = Ventana()
