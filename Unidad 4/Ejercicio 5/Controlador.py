from urllib.request import urlopen
import json
import requests
from Modelos import Pelicula

class ManejadorPelicula():
    __peliculas: list
    def __init__(self):
        url = "https://api.themoviedb.org/3/discover/movie?api_key=6e34ecc32a269e5c833d98f535c71aa1"
        response = requests.get(url)
        data = response.json()
        self.__pelis = data['results']
        self.__peliculas=[]
    def agregarPeli(self,unaPeli):
        self.__peliculas.append(unaPeli)
    def cargaPeli(self):
        for movies in self.__pelis:
            lenguaje = movies['original_language']
            titulo = movies['original_title']
            resumen = movies['overview']
            fecha = movies['release_date']
            unaPeli = Pelicula(lenguaje,titulo,resumen,fecha)
            self.agregarPeli(unaPeli)
    def Mostrar(self):
        for i in range(len(self.__listaPelis)):
            print("Nombre: ", self.__listaPelis[i].getTit())
    def seleccionarPeli(self, index):
        self.seleccion = index
        contacto = self.contactos[index]
        self.vista.verPeliculaEnForm(Pelicula)
    def getPelis(self):
        return self.__peliculas