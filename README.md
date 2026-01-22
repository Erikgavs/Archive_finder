# 🔍 Archive Finder

Herramienta de búsqueda de archivos diseñada para facilitar la enumeración en entornos de pentesting y CTF.

## 📋 Descripción

Archive Finder es un script en Python que permite buscar archivos por nombre en el sistema de manera rápida y visual. Diseñado específicamente para ayudar en la fase de enumeración durante auditorías de seguridad y desafíos CTF.

## ✨ Características

- 🔎 Búsqueda por nombre de archivo (coincidencia parcial)
- 🎯 Opción de buscar en todo el sistema o en una ruta específica
- 🎨 Salida colorizada para mejor visualización
- ⚡ Interfaz interactiva y fácil de usar
- 🐧 Compatible con sistemas Linux

## 🛠️ Requisitos

- Python 3.x
- Sistema operativo Linux
- Permisos de lectura en los directorios a escanear (se recomienda ejecutar con sudo para acceso completo)

## 📥 Instalación

```bash
git clone https://github.com/Erikgavs/Archive_finder.git
cd Archive_finder
```

## 🚀 Uso

### Ejecución básica

```bash
python3 finder.py
```

### Ejecución con privilegios elevados (recomendado)

```bash
sudo python3 finder.py
```

### Ejemplos de uso

**1. Búsqueda en todo el sistema:**
```bash
$ python3 finder.py

Proporciona el nombre del archivo que estás buscando: config.php

Quieres buscar en una Ruta específica? (S/N): N
[*] Seguiremos con el procedimiento normal
[*] Archivo encontrado: config.php /var/www/html
[*] Archivo encontrado: config.php /opt/app/includes
```

**2. Búsqueda en ruta específica:**
```bash
$ python3 finder.py

Proporciona el nombre del archivo que estás buscando: password

Quieres buscar en una Ruta específica? (S/N): S
[*] Específica la ruta: /home/user
[*] Ruta especificada: /home/user
[*] Archivo encontrado: passwords.txt /home/user/Documents
```

## ⚠️ Limitaciones Conocidas

- Los errores de permisos no se muestran en pantalla
- No soporta búsquedas por expresiones regulares
- No permite búsqueda por múltiples términos simultáneamente
- No puede buscar por permisos, tamaño o fecha de modificación
- La búsqueda distingue entre mayúsculas y minúsculas

## 🔒 Advertencia Legal

Este script está diseñado **exclusivamente para uso ético** en:
- Entornos controlados de laboratorio
- Plataformas de práctica autorizadas (HackTheBox, TryHackMe, etc.)
- Auditorías de seguridad con autorización explícita
- Competiciones CTF

**NO** debe ser usado para:
- Acceder a sistemas sin autorización
- Causar daño o perjuicio a terceros
- Actividades ilegales de cualquier tipo

El uso indebido de esta herramienta es responsabilidad exclusiva del usuario.

## 👤 Autor

**Erik**

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

*Herramienta creada con fines educativos y de seguridad ética.*
