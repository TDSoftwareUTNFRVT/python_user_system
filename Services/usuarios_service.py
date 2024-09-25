import os
from Clases.usuario import Usuario

# Ruta del archivo de usuarios
ruta_archivo = os.path.join(os.path.dirname(__file__), '../Datos/usuarios.txt')

def leer_usuarios():
    usuarios = []
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                usuarios.append(Usuario.from_string(linea))
    return usuarios

def agregar_usuario(usuario):
    with open(ruta_archivo, 'a') as archivo:
        archivo.write(str(usuario) + '\n')

def actualizar_usuario(dni, nuevos_datos):
    usuarios = leer_usuarios()
    with open(ruta_archivo, 'w') as archivo:
        for usuario in usuarios:
            if usuario.dni == dni:
                archivo.write(str(Usuario(*nuevos_datos)) + '\n')
            else:
                archivo.write(str(usuario) + '\n')

def eliminar_usuario(dni):
    usuarios = leer_usuarios()
    with open(ruta_archivo, 'w') as archivo:
        for usuario in usuarios:
            if usuario.dni != dni:
                archivo.write(str(usuario) + '\n')