def leer_archivo_por_caracter(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            while True:
                caracter = archivo.read(1)  # Lee un carácter
                if not caracter:  # Si no hay más caracteres, termina el bucle
                    break
                print(caracter, end='')  # Imprime el carácter en consola
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def texto(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contenido