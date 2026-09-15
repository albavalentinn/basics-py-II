"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""

# Lista global de prueba que usaremos para probar las funciones
mis_libros = []


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""
def agregar_libro(titulo, autor):
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor
    }
    return nuevo_libro

# Prueba la función con algunos valores
libro1 = agregar_libro("1984", "George Orwell")
libro2 = agregar_libro("Rebelión en la granja", "George Orwell")
libro3 = agregar_libro("El nombre de la rosa", "Umberto Eco")

# Añadimos los diccionarios a nuestra lista de prueba
mis_libros.append(libro1)
mis_libros.append(libro2)
mis_libros.append(libro3)

print("--- Ejercicio 1 ---")
print("Libro creado:", libro1)
print()


"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""
def listar_libros(libros):
    lista_titulos = []
    for libro in libros:
        lista_titulos.append(libro["titulo"])
    return lista_titulos

# Prueba la función con algunos valores
print("--- Ejercicio 2 ---")
titulos_actuales = listar_libros(mis_libros)
print("Lista de títulos:", titulos_actuales)
print()


"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""
def buscar_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            return libro
    return None

# Prueba la función con algunos valores
print("--- Ejercicio 3 ---")
libro_encontrado = buscar_libro(mis_libros, "1984")
print("Buscando '1984':", libro_encontrado)
libro_no_encontrado = buscar_libro(mis_libros, "El Quijote")
print("Buscando 'El Quijote':", libro_no_encontrado)
print()


"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""
def quitar_libro(libros, titulo):
    libro_a_borrar = buscar_libro(libros, titulo) # Usamos la función del ejercicio 3
    
    try:
        if libro_a_borrar is None:
            raise ValueError(f"El libro '{titulo}' no está en la lista.")
        libros.remove(libro_a_borrar)
        print(f"Éxito: El libro '{titulo}' ha sido eliminado.")
    except ValueError as error:
        print(f"Error capturado: {error}")

# Prueba la función con algunos valores
print("--- Ejercicio 4 ---")
quitar_libro(mis_libros, "El nombre de la rosa") # Este existe, lo borra
quitar_libro(mis_libros, "Harry Potter") # Este no existe, salta el error manejado
print()


"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""
def crear_inventario(libros):
    inventario = {}
    for libro in libros:
        autor = libro["autor"]
        if autor in inventario:
            inventario[autor] += 1
        else:
            inventario[autor] = 1
    return inventario

# Prueba la función con algunos valores
print("--- Ejercicio 5 ---")
inventario_autores = crear_inventario(mis_libros)
print("Inventario por autor:", inventario_autores)
print()


"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""
def libros_por_autor(libros, autor):
    titulos = []
    for libro in libros:
        if libro["autor"] == autor:
            titulos.append(libro["titulo"])
    return titulos

# Prueba la función con algunos valores
print("--- Ejercicio 6 ---")
libros_orwell = libros_por_autor(mis_libros, "George Orwell")
print("Libros de George Orwell:", libros_orwell)
print()


"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""
def existe_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            return True
    return False

# Prueba la función con algunos valores
print("--- Ejercicio 7 ---")
print("¿Existe '1984'?:", existe_libro(mis_libros, "1984"))
print("¿Existe 'Harry Potter'?:", existe_libro(mis_libros, "Harry Potter"))