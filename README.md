# 🔍 Archive Finder

File search tool designed to facilitate enumeration in pentesting and CTF environments.

## 📋 Description

Archive Finder is a Python script that allows you to search for files by name on the system quickly and visually. Specifically designed to assist in the enumeration phase during security audits and CTF challenges.

## ✨ Features

- 🔎 Search by filename (partial match)
- 🎯 Option to search the entire system or a specific path
- 🎨 Colorized output for better visualization
- ⚡ Interactive and easy-to-use interface
- 🐧 Linux compatible

## 🛠️ Requirements

- Python 3.x
- Linux operating system
- Read permissions on directories to scan (recommended to run with sudo for full access)

## 📥 Installation

```bash
git clone https://github.com/Erikgavs/Archive_finder.git
cd Archive_finder
```

## 🚀 Usage

### Basic execution

```bash
python3 finder.py
```

### Execution with elevated privileges (recommended)

```bash
sudo python3 finder.py
```

### Usage examples

**1. System-wide search:**
```bash
$ python3 finder.py

Proporciona el nombre del archivo que estás buscando: config.php

Quieres buscar en una Ruta específica? (S/N): N
[*] Seguiremos con el procedimiento normal
[*] Archivo encontrado: config.php /var/www/html
[*] Archivo encontrado: config.php /opt/app/includes
```

**2. Specific path search:**
```bash
$ python3 finder.py

Proporciona el nombre del archivo que estás buscando: password

Quieres buscar en una Ruta específica? (S/N): S
[*] Específica la ruta: /home/user
[*] Ruta especificada: /home/user
[*] Archivo encontrado: passwords.txt /home/user/Documents
```

## ⚠️ Known Limitations

- Permission errors are not displayed on screen
- Does not support regular expression searches
- Does not allow searching for multiple terms simultaneously
- Cannot search by permissions, size, or modification date
- Search is case-sensitive

## 🔒 Legal Warning

This script is designed **exclusively for ethical use** in:
- Controlled laboratory environments
- Authorized practice platforms (HackTheBox, TryHackMe, etc.)
- Security audits with explicit authorization
- CTF competitions

**DO NOT** use it for:
- Accessing systems without authorization
- Causing harm or damage to third parties
- Illegal activities of any kind

Misuse of this tool is the sole responsibility of the user.

## 👤 Author

**Erik**

## 📄 License

This project is open source and available for educational use.

---

*Tool created for educational and ethical security purposes.*
