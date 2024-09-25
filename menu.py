import tkinter as tk
from tkinter import messagebox
from Services import usuarios_service, ventana_service
from Clases.usuario import Usuario



import tkinter as tk
from tkinter import messagebox
from Services import usuarios_service
from Services import ventana_service
from Clases.usuario import Usuario

def iniciar_sesion():
    def verificar_credenciales():
        mail = entry_mail.get()
        dni = entry_dni.get()
        usuarios = usuarios_service.leer_usuarios()
        for usuario in usuarios:
            if usuario.mail == mail and usuario.dni == dni:
                ventana_login.destroy()
                menu_principal()
                return
        messagebox.showerror("Error", "Credenciales incorrectas")

    ventana_login = tk.Tk()
    ventana_login.geometry("300x200")
    ventana_login.title("Inicio de Sesión")

    frame_login = tk.Frame(ventana_login)
    frame_login.place(relx=0.5, rely=0.5, anchor="center")

    titulo_login = tk.Label(frame_login, text="Inicio de Sesión", font=("Arial", 14))
    titulo_login.grid(row=0, column=0, columnspan=2, pady=10)

    label_mail = tk.Label(frame_login, text="Mail", font=("Arial", 10))
    label_mail.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_mail = tk.Entry(frame_login, font=("Arial", 10))
    entry_mail.grid(row=1, column=1, padx=10, pady=5)

    label_dni = tk.Label(frame_login, text="DNI", font=("Arial", 10))
    label_dni.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_dni = tk.Entry(frame_login, font=("Arial", 10))
    entry_dni.grid(row=2, column=1, padx=10, pady=5)

    boton_login = tk.Button(frame_login, text="Iniciar Sesión", command=verificar_credenciales, width=20)
    boton_login.grid(row=3, column=0, columnspan=2, pady=10)

    ventana_login.mainloop()


def menu_principal():
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Menú Principal")

    titulo = tk.Label(root, text="Sistema de Gestión de Usuarios", font=("Arial", 16))
    titulo.pack(pady=20)

    def nuevo_usuario():
        nueva_ventana = tk.Toplevel(root)
        nueva_ventana.title("Nuevo Usuario")
        nueva_ventana.geometry("400x450")

        frame_formulario = tk.Frame(nueva_ventana)
        frame_formulario.place(relx=0.5, rely=0.5, anchor="center")

        titulo_formulario = tk.Label(frame_formulario, text="Nuevo Usuario", font=("Arial", 14))
        titulo_formulario.grid(row=0, column=0, columnspan=2, pady=10)

        campos = ["Apellidos", "Nombres", "DNI", "Fecha Nacimiento", "Domicilio", "Localidad", "Provincia", "Codigo Postal", "Telefonos", "Mail"]
        entradas = {}

        for i, campo in enumerate(campos):
            label = tk.Label(frame_formulario, text=campo, font=("Arial", 10))
            label.grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(frame_formulario, font=("Arial", 10))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entradas[campo] = entry

        def guardar_usuario():
            usuario = ventana_service.guardar_usuario(entradas)
            usuarios_service.agregar_usuario(usuario)
            messagebox.showinfo("Éxito", "Usuario agregado correctamente")
            nueva_ventana.destroy()

        boton_guardar = tk.Button(frame_formulario, text="Guardar", command=guardar_usuario)
        boton_guardar.grid(row=len(campos)+1, column=0, columnspan=2, pady=10)

    def listar_usuarios():
        nueva_ventana = tk.Toplevel(root)
        nueva_ventana.title("Lista de Usuarios")
        nueva_ventana.geometry("600x400")

        usuarios = usuarios_service.leer_usuarios()

        frame_lista = tk.Frame(nueva_ventana)
        frame_lista.pack(fill=tk.BOTH, expand=True)

        for i, usuario in enumerate(usuarios):
            for j, dato in enumerate(str(usuario).split(',')):
                label = tk.Label(frame_lista, text=dato, borderwidth=1, relief="solid", font=("Arial", 10))
                label.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

    def actualizar_usuario():
        nueva_ventana = tk.Toplevel(root)
        nueva_ventana.title("Actualizar Usuario")
        nueva_ventana.geometry("400x200")

        frame_formulario = tk.Frame(nueva_ventana)
        frame_formulario.place(relx=0.5, rely=0.5, anchor="center")

        titulo_formulario = tk.Label(frame_formulario, text="Actualizar Usuario", font=("Arial", 14))
        titulo_formulario.grid(row=0, column=0, columnspan=2, pady=10)

        label_dni = tk.Label(frame_formulario, text="DNI", font=("Arial", 10))
        label_dni.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_dni = tk.Entry(frame_formulario, font=("Arial", 10))
        entry_dni.grid(row=1, column=1, padx=10, pady=5)

        def buscar_usuario():
            dni = entry_dni.get()
            usuarios = usuarios_service.leer_usuarios()
            for usuario in usuarios:
                if usuario.dni == dni:
                    nueva_ventana.geometry("400x450")
                    for widget in frame_formulario.winfo_children():
                        widget.destroy()

                    titulo_formulario = tk.Label(frame_formulario, text="Actualizar Usuario", font=("Arial", 14))
                    titulo_formulario.grid(row=0, column=0, columnspan=2, pady=10)

                    campos = ["Apellidos", "Nombres", "DNI", "Fecha Nacimiento", "Domicilio", "Localidad", "Provincia", "Codigo Postal", "Telefonos", "Mail"]
                    entradas = {}

                    for i, campo in enumerate(campos):
                        label = tk.Label(frame_formulario, text=campo, font=("Arial", 10))
                        label.grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
                        entry = tk.Entry(frame_formulario, font=("Arial", 10))
                        entry.grid(row=i+1, column=1, padx=10, pady=5)
                        entradas[campo] = entry
                        entradas[campo].insert(0, getattr(usuario, campo.lower().replace(' ', '_')))

                    def guardar_cambios():
                        nuevos_datos = [
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
                        ]
                        usuarios_service.actualizar_usuario(dni, nuevos_datos)
                        messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                        nueva_ventana.destroy()

                    boton_guardar = tk.Button(frame_formulario, text="Guardar Cambios", command=guardar_cambios)
                    boton_guardar.grid(row=len(campos)+1, column=0, columnspan=2, pady=10)
                    return

            messagebox.showerror("Error", "Usuario no encontrado")

        boton_buscar = tk.Button(frame_formulario, text="Buscar", command=buscar_usuario)
        boton_buscar.grid(row=2, column=0, columnspan=2, pady=10)

    def eliminar_usuario():
        nueva_ventana = tk.Toplevel(root)
        nueva_ventana.title("Eliminar Usuario")
        nueva_ventana.geometry("300x200")

        frame_formulario = tk.Frame(nueva_ventana)
        frame_formulario.place(relx=0.5, rely=0.5, anchor="center")

        titulo_formulario = tk.Label(frame_formulario, text="Eliminar Usuario", font=("Arial", 14))
        titulo_formulario.grid(row=0, column=0, columnspan=2, pady=10)

        label_dni = tk.Label(frame_formulario, text="DNI", font=("Arial", 10))
        label_dni.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_dni = tk.Entry(frame_formulario, font=("Arial", 10))
        entry_dni.grid(row=1, column=1, padx=10, pady=5)

        def eliminar():
            dni = entry_dni.get()
            usuarios_service.eliminar_usuario(dni)
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
            nueva_ventana.destroy()

        boton_eliminar = tk.Button(frame_formulario, text="Eliminar", command=eliminar)
        boton_eliminar.grid(row=2, column=0, columnspan=2, pady=10)

    def salir():
        root.quit()

    ancho_boton=35
    boton_nuevo = tk.Button(root, text="Nuevo Usuario", command=nuevo_usuario, width=ancho_boton)
    boton_nuevo.pack(pady=10)

    boton_listar = tk.Button(root, text="Listar Usuarios", command=listar_usuarios, width=ancho_boton)
    boton_listar.pack(pady=10)

    boton_actualizar = tk.Button(root, text="Actualizar Usuario", command=actualizar_usuario, width=ancho_boton)
    boton_actualizar.pack(pady=10)

    boton_eliminar = tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario, width=ancho_boton)
    boton_eliminar.pack(pady=10)


    boton_salir = tk.Button(root, text="Salir", command=salir, width=ancho_boton)
    boton_salir.pack(pady=10)

    root.mainloop()

iniciar_sesion()