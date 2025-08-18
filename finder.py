
import os 


print(r"""           
________ 0    ||    |   |||      ______     |||||            
|             | |   |   |  ||    |          |   ||            
|___     |    |  |  |   |    |   |__        |  ||             
|        |    |   | |   |  ||    |          |   ||           
|        |    |    ||   |||      |_____     |    ||  

[*] Tool designed by Erik
[*] Tool designed for ethical pourposes
""")

reset = "\033[0m"

azul = "\033[34m"

palabra = input("\nProporciona el nombre del archivo que estás buscando: ")

ruta = input(f"\nQuieres buscar en una Ruta específica? {azul}(S/N){reset}: ")

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
            print(f"[*] Archivo encontrado: {azul}{archivo}{reset}")
            encontrado = True
if not encontrado:
    print("[-] Archivo no encontrado")
    exit()

