from blog import Blog

def main():
    blog = Blog()
    while True:
        print("\nMenú:")
        print("1. Ingresar un nuevo Post")
        print("2. Modificar un Post")
        print("3. Mostrar todos los Post")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Ingresar un nuevo Post
            blog.agregarPost()
        elif opcion == "2":
            # Modificar un valor existente
            if not blog.lista:
                print("No hay Post en el Blog.")
            else:
                print("Post actuales:")
                for i, v in enumerate(blog.lista):
                    print(f"{i + 1}. {v}")
                indice = int(input("Seleccione el Post a modificar: ")) - 1
                if 0 <= indice < len(blog.lista):
                    blog.modificarPost(indice)
                else:
                    print("Índice inválido.")
        elif opcion == "3":
            # Mostrar todos los Posts
            if blog.lista:
                blog.mostrarTodos()
            else:
                print("No hay Posts subidos al Blog.")
        elif opcion == "4":
            # Mostrar desde una fecha en particular
            if blog.lista:
                blog.mostrarDesde()
            else:
                print("No hay Post en El Blog.")
        elif opcion == "5":
            # Mostrar hasta una fecha en particular
            if blog.lista:
                blog.mostrarHasta()
            else:
                print("No hay Post en El Blog.")
        elif opcion == "6":
            # Mostrar desde una fecha y hasta una fecha en particular
            if blog.lista:
                blog.mostrarDesdeHasta()
            else:
                print("No hay Post en El Blog.")
        elif opcion == "7":
            # Salir
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
    
if __name__ == "__main__":
    main()