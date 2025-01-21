from post import Post
from fecha import Fecha

class Blog:
    def __init__(self):
        self.lista = []

    def agregarPost(self):
        titulo = input("Ingrese titulo: ")
        contenido = input("Ingrese contenido del Post: ")
        post = Post(titulo, contenido)
        self.lista.append(post)

    def mostrarTodos(self):
        for post in self.lista:
            print (post)

    def mostrarDesde(self):
        print("Ingrese fecha:")
        anio = input("anio: ")
        mes = input("mes: ")
        dia = input("dia: ")
        fecha_ingresada = Fecha(f"{anio}-{mes}-{dia}").fecha

        print(f"Post de fechas ingresadas a partir de {fecha_ingresada.strftime('%d/%m/%Y')}:")

        for post in self.lista:
            if post.getFecha() >= fecha_ingresada:
                print(post)
                
    def mostrarHasta(self):
        print("Ingrese fecha:")
        anio = input("anio: ")
        mes = input("mes: ")
        dia = input("dia: ")
        fecha_ingresada = Fecha(f"{anio}-{mes}-{dia}").fecha

        print(f"Post de fechas ingresadas hasta {fecha_ingresada.strftime('%d/%m/%Y')}:")

        for post in self.lista:
            if post.getFecha() <= fecha_ingresada:
                print(post)
    
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

        print(f"Post de fechas ingresadas a partir de {fecha_ingresada.strftime('%d/%m/%Y')} hasta {segunda_fecha.strftime('%d/%m/%Y')}:")

        for post in self.lista:
            if post.getFecha() >= fecha_ingresada:
                if post.getFecha() <= segunda_fecha:
                    print(post)