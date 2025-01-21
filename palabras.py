import unicodedata
import re

class Palabras:
    def __init__(self):
        pass
    
    def slugs(self, texto):
        texto_normalizado = unicodedata.normalize('NFKD', texto) # eliminar los acentos
        texto_ascii = texto_normalizado.encode('ascii', 'ignore').decode('utf-8') #elimina caracteres especiales
        texto_slugs = re.sub(r'[\s-]+', '-', texto_ascii).strip('-')
        return texto_slugs
    
    def unir_palabras(self, texto1, texto2):
        return (texto1 + "-" + texto2)
    
    def frase_mayuscula(self, texto):
        return texto.upper()
    
    def frase_minuscula(self, texto):
        return texto.lower()