
import os 

# HACER ENCABEZADO CON TEXTO ASCII
print(r"""           
________ 0    ||    |   |||      ______     ||||            
|             | |   |   |  ||    |          |   ||            
|___     |    |  |  |   |    |   |__        |  ||             
|        |    |   | |   |  ||    |          |   ||           
|        |    |    ||   |||      |_____     |    ||         
""")


# CONTENIDO DEL SCRIPT

palabra = input("\nProporciona el nombre del archivo que estás buscando: ")

ruta = "/"
encontrado = False

for raiz, carpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        if palabra in archivo:
            print(f"[*] Archivo encontrado {archivo}")
            encontrado = True
if not encontrado:
    print("[-] Archivo no encontrado")
    exit()

