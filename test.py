from Refuerzo.palabras import Palabras
from fecha import Fecha
from Refuerzo.post import Post
from datetime import datetime

def main():
    """
    texto = Palabras()
    entrada = input("ingrese: ")
    print(str(texto.slugs(entrada)))
    print(texto.frase_mayuscula(entrada))
    fecha = Fecha()
    print (fecha.fecha_formateada())
    fecha_hora1 = datetime(2025, 1, 18, 14, 30)
    fecha_hora2 = datetime(2025, 1, 18, 10, 0)
    
    fecha1 = datetime.now()
    fecha2 = datetime.now()
    fecha = Fecha()
    print (fecha.mayor(fecha1, fecha2))
    """
    post = Post("post1", "contenido1")
    fecha1 = datetime(2025, 1, 1)
    fecha2 = post.getFecha()
    fecha = Fecha()
    print (fecha.mayor(fecha1, fecha2))

if __name__ == "__main__":
    main()