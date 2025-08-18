
import os 


print(r"""           
________ 0    ||    |   |||      ______     |||||            
|             | |   |   |  ||    |          |   ||            
|___     |    |  |  |   |    |   |__        |  ||             
|        |    |   | |   |  ||    |          |   ||           
|        |    |    ||   |||      |_____     |    ||  

[*] Tool designed by Erik
[*] Tool designed for ethical pourposes and may not be used to do illegal things 
[*] Enumerate the archives of a machine 
""")

# CONTENIDO DEL SCRIPT

palabra = input("\nProporciona el nombre del archivo que estás buscando: ")

ruta = input("\nQuieres buscar en una Ruta específica? (S/N): ")

if ruta.upper() == "S":
    ruta = input("[*] Específica la ruta: ")
    print(f"[*] Ruta específicada: {ruta}")
else:
    ruta = "/"
    print("[*] Seguiremos con el procedimiento normal")


encontrado = False

for raiz, carpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        if palabra in archivo:
            print(f"[*] Archivo encontrado: {archivo}")
            encontrado = True
if not encontrado:
    print("[-] Archivo no encontrado")
    exit()

