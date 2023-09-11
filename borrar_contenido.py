import os # proporciona funciones para interactuar con el sistema operativo, como manipular archivos y directorios

def borrar_contenido(carpeta):
    for nombre_archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)
        elif os.path.isdir(ruta_archivo):
            borrar_contenido(ruta_archivo)
            # Si deseas mantener las subcarpetas vacías, comenta la línea siguiente
            #os.rmdir(ruta_archivo)

# Ejemplo de uso
directorio_raiz = "D:\Dewalt\Trimmer"

# Llama a la función para eliminar el contenido de las carpetas sin borrar las subcarpetas
borrar_contenido(directorio_raiz)
