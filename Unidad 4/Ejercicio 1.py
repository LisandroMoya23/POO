from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
	__ventana:None
	def __init__(self):
		self.__ventana=Tk()
		self.__ventana.title('Calculadora IPC')

		self.mainframe = Frame()
		self.mainframe.pack()
		self.mainframe.configure(bg='gray87')
		ttk.Label(self.mainframe, text="Item", background='gray87').grid(column=0, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Cantidad",background='gray87').grid(column=1, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Precio Año Base",background='gray87').grid(column=2, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Precio Año Actual", background='gray87').grid(column=3, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Vestimenta", background='gray87').grid(column=0, row=1, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Alimentos", background='gray87').grid(column=0, row=2, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Educacion", background='gray87').grid(column=0, row=3, padx=10, pady=10)


		self.cantVest = Entry(self.mainframe)
		self.cantVest.grid(padx=10, pady=10, row=1, column=1)

		self.precioBVest = Entry(self.mainframe)
		self.precioBVest.grid(padx=10, pady=10, row=1, column=2)

		self.precioAVest = Entry(self.mainframe)
		self.precioAVest.grid(padx=10, pady=10, row=1, column=3)

		self.cantAlim=Entry(self.mainframe)
		self.cantAlim.grid(padx=10, pady=10, row=2, column=1)

		self.precioBAlim=Entry(self.mainframe)
		self.precioBAlim.grid(padx=10, pady=10, row=2, column=2)

		self.precioAAlim=Entry(self.mainframe)
		self.precioAAlim.grid(padx=10, pady=10, row=2, column=3)

		self.cantEdu=Entry(self.mainframe)
		self.cantEdu.grid(padx=10, pady=10, row=3, column=1)

		self.precioBEdu=Entry(self.mainframe)
		self.precioBEdu.grid(padx=10, pady=10, row=3, column=2)

		self.precioAEdu=Entry(self.mainframe)
		self.precioAEdu.grid(padx=10, pady=10, row=3, column=3)

		Button(self.mainframe, text="Calcular IPC", command=self.calcular).grid(column=1, row=5, pady=10, padx=10)
		Button(self.mainframe, text='Salir', command=self.__ventana.destroy, width=10).grid(column=2, row=5, pady=10, padx=10)
		ttk.Label(self.mainframe, text='IPC %', background='gray87').grid(column=0, row=6, padx=10, pady=10)
		
		self.__ventana.mainloop()
	def calcular(self):
		try:
			costoBase=float((int(self.cantVest.get())*int(self.precioBVest.get()))+(int(self.cantEdu.get())*int(self.precioBEdu.get()))+(int(self.cantAlim.get())*int(self.precioBAlim.get())))
			costoActual=float((int(self.cantVest.get())*int(self.precioAVest.get()))+(int(self.cantEdu.get())*int(self.precioAEdu.get()))+(int(self.cantAlim.get())*int(self.precioAAlim.get())))
			total=int((costoActual/costoBase)*100)
			total=str(total)+'%'
			ttk.Label(self.mainframe, text=total, background='gray87').grid(column=1, row=6, padx=10, sticky=W)
			
			
		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor en todas las casillas')
if __name__ == '__main__':
	ventana=Aplicacion()