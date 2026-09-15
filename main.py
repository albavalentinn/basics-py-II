# Importamos todas las funciones que creaste en el archivo libreria.py
import libreria

# Añade una colección de libros
# Creamos una lista vacía y le vamos añadiendo libros con tu función
mi_coleccion = []
mi_coleccion.append(libreria.agregar_libro("Dune", "Frank Herbert"))
mi_coleccion.append(libreria.agregar_libro("El Mesías de Dune", "Frank Herbert"))
mi_coleccion.append(libreria.agregar_libro("Fahrenheit 451", "Ray Bradbury"))
mi_coleccion.append(libreria.agregar_libro("Fundación", "Isaac Asimov"))


# Muestra la colección de libros creada
print("--- Colección Actual ---")
titulos = libreria.listar_libros(mi_coleccion)
print(titulos)


# Busca un libro por el autor
print("\n--- Búsqueda por Autor ---")
libros_herbert = libreria.libros_por_autor(mi_coleccion, "Frank Herbert")
print(f"Libros encontrados de Frank Herbert: {libros_herbert}")


# Verifica si un libro está disponible
print("\n--- Verificación de Disponibilidad ---")
existe_fundacion = libreria.existe_libro(mi_coleccion, "Fundación")
existe_quijote = libreria.existe_libro(mi_coleccion, "Don Quijote")

print(f"¿Tenemos 'Fundación'?: {existe_fundacion}")
print(f"¿Tenemos 'Don Quijote'?: {existe_quijote}")