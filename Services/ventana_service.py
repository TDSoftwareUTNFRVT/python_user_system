from Clases.usuario import Usuario

def guardar_usuario(entradas):
    usuario = Usuario(
        entradas["Apellidos"].get(),
        entradas["Nombres"].get(),
        entradas["DNI"].get(),
        entradas["Fecha Nacimiento"].get(),
        entradas["Domicilio"].get(),
        entradas["Localidad"].get(),
        entradas["Provincia"].get(),
        entradas["Codigo Postal"].get(),
        entradas["Telefonos"].get(),
        entradas["Mail"].get()
    )
    return usuario