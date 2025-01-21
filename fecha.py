from datetime import datetime

class Fecha:    
    def __init__(self, fecha = None):
        if isinstance(fecha, str):
            self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        elif isinstance(fecha, datetime):
            self.fecha = fecha
        else:
            self.fecha = datetime.now()
    
    def fecha_formateada(self):
        formato = "%d/%m/%Y"
        return self.fecha.strftime(formato)
    
    def menor(self, fecha1, fecha2):
        return fecha1 < fecha2 
    
    def mayor(self, fecha1, fecha2):
        return fecha1 > fecha2
    
    def __str__(self):
        return self.fecha_formateada()