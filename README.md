# Limpieza de Contenido de Directorios en Python

Este es un simple script en Python que permite eliminar el contenido de un directorio, incluyendo archivos y subdirectorios. También puedes optar por eliminar las subcarpetas vacías si lo deseas.

## Uso

1. Asegúrate de tener Python instalado en tu sistema.

2. Clona o descarga este repositorio en tu máquina local.

3. Abre el archivo `borrar_contenido.py` en un editor de texto o un entorno de desarrollo Python.

4. Modifica la variable `directorio_raiz` con la ruta del directorio que deseas limpiar.

5. Ejecuta el script `borrar_contenido.py` en tu terminal o IDE favorito.

6. El contenido del directorio especificado será eliminado.

**Nota:** Ten en cuenta que este script puede borrar permanentemente archivos y directorios, así que úsalo con precaución.

## Personalización

Si deseas mantener las subcarpetas vacías después de eliminar su contenido, puedes descomentar la línea siguiente en el script:

```python
#os.rmdir(ruta_archivo)
