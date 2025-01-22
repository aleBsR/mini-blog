from post import Post
from fecha import Fecha
from datetime import datetime

class Blog:
    def __init__(self):
        self.lista = []

    def agregarPost(self):
        titulo = self.validar_titulo()
        contenido = self.validar_contenido()
        post = Post(titulo, contenido)
        self.lista.append(post)

    def modificarPost(self, posicion):
        titulo = self.validar_titulo()
        contenido = self.validar_contenido()
        fecha_ingresada = self.ingresar_fecha()
        post = Post(titulo, contenido, fecha_ingresada.fecha)
        self.lista[posicion] = post
        
    def modificarTitulo(self, posicion):
        contenido = self.lista[posicion].contenido
        fecha = self.lista[posicion].getFecha()
        titulo = self.validar_titulo()
        post = Post(titulo, contenido, fecha)
        self.lista[posicion] = post
        
    def modificarContenido(self, posicion):
        titulo = self.lista[posicion].titulo
        fecha = self.lista[posicion].getFecha()
        contenido = self.validar_contenido()
        post = Post(titulo, contenido, fecha)
        self.lista[posicion] = post
        
    def modificarFecha(self, posicion):
        titulo = self.lista[posicion].titulo
        contenido = self.lista[posicion].contenido
        fecha_ingresada = self.ingresar_fecha()
        post = Post(titulo, contenido, fecha_ingresada.fecha)
        self.lista[posicion] = post
    
    def mostrarTodos(self):
        for post in self.lista:
            print (post)

    def mostrarDesde(self):
        print("Ingrese fecha:")
        anio = input("anio: ")
        mes = input("mes: ")
        dia = input("dia: ")
        fecha_ingresada = Fecha(f"{anio}-{mes}-{dia}").fecha

        control = False

        print(f"Post de fechas ingresadas a partir de {fecha_ingresada.strftime('%d/%m/%Y')}:")

        for post in self.lista:
            if post.getFecha() >= fecha_ingresada:
                control = True
                print(post)
                
        if control == False:
            print (f"No hay fechas ingresadas desde {fecha_ingresada.strftime('%d/%m/%Y')}")
                
    def mostrarHasta(self):
        print("Ingrese fecha:")
        anio = input("anio: ")
        mes = input("mes: ")
        dia = input("dia: ")
        fecha_ingresada = Fecha(f"{anio}-{mes}-{dia}").fecha

        control = False

        print(f"Post de fechas ingresadas hasta {fecha_ingresada.strftime('%d/%m/%Y')}:")

        for post in self.lista:
            if post.getFecha() <= fecha_ingresada:
                control = True
                print(post)
    
        if control == False:
            print (f"No hay fechas ingresadas hasta {fecha_ingresada.strftime('%d/%m/%Y')}")
            
    def mostrarDesdeHasta(self):
        print("Ingrese fecha desde la que quiere buscar:")
        anio = input("anio: ")
        mes = input("mes: ")
        dia = input("dia: ")
        fecha_ingresada = Fecha(f"{anio}-{mes}-{dia}").fecha
        
        print("Ingrese fecha hasta la que quiere buscar:")
        anio2 = input("anio: ")
        mes2 = input("mes: ")
        dia2 = input("dia: ")
        segunda_fecha = Fecha(f"{anio2}-{mes2}-{dia2}").fecha

        control = False

        print(f"Post de fechas ingresadas a partir de {fecha_ingresada.strftime('%d/%m/%Y')} hasta {segunda_fecha.strftime('%d/%m/%Y')}:")

        for post in self.lista:
            if post.getFecha() >= fecha_ingresada:
                if post.getFecha() <= segunda_fecha:
                    control = True
                    print(post)
                    
        if control == False:
            print (f"No hay fechas ingresadas entre {fecha_ingresada.strftime('%d/%m/%Y')} y {segunda_fecha.strftime('%d/%m/%Y')}")
            
    def validar_titulo(self):
        while True:
            titulo = input("Ingrese el título: ").strip()
            if len(titulo) < 5:
                print("El título debe tener al menos 5 caracteres.")
            elif len(titulo) > 100:
                print("El título no debe exceder los 100 caracteres.")
            else:
                return titulo
    def validar_contenido(self):
        while True:
            contenido = input("Ingrese el contenido del Post: ").strip()
            if not contenido:
                print("El contenido no puede estar vacío.")
            elif len(contenido) > 500:
                print("El contenido no debe exceder los 500 caracteres.")
            else:
                return contenido
            
    def ingresar_fecha(self):
        while True:
            try:
                fecha_ingresada = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
                return Fecha(fecha_ingresada)  # Intenta crear un objeto Fecha
            except ValueError:
                print("Fecha inválida. Asegúrese de usar el formato YYYY-MM-DD.")


