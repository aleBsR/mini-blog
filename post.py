from fecha import Fecha

class Post:
    def __init__(self, titulo, contenido, fecha = None):
        self.titulo = titulo
        self.contenido = contenido
        self.fecha = Fecha(fecha)

    def __str__(self):
        return f"{self.titulo}: {self.contenido}. Creado: {self.fecha}"
    
    def getFecha(self):
        return self.fecha.fecha