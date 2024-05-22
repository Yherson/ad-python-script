import os
import sys
import webbrowser
import winreg as reg

# URL de la página web
url = "https://queropalca.netlify.app/"

# Función para abrir la página web
def open_webpage():
    webbrowser.open(url)

# Función para añadir el script al inicio de Windows
def add_to_startup():
    # Ruta absoluta al script de Python
    script_path = os.path.abspath(sys.argv[0])

    # Nombre de la clave en el registro
    key_name = "OpenWebPage"

    # Abrir la clave de registro para ejecutar programas al inicio
    key = reg.HKEY_CURRENT_USER
    sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    with reg.OpenKey(key, sub_key, 0, reg.KEY_SET_VALUE) as key_handle:
        reg.SetValueEx(key_handle, key_name, 0, reg.REG_SZ, script_path)

# Comprobar si el script ya está registrado para ejecutarse al inicio
def is_added_to_startup():
    key = reg.HKEY_CURRENT_USER
    sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    try:
        with reg.OpenKey(key, sub_key, 0, reg.KEY_READ) as key_handle:
            value, _ = reg.QueryValueEx(key_handle, "OpenWebPage")
            return value == os.path.abspath(sys.argv[0])
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    if not is_added_to_startup():
        add_to_startup()
    open_webpage()
