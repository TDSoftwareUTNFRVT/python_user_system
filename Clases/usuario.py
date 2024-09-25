class Usuario:
    def __init__(self, apellidos, nombres, dni, fecha_nacimiento, domicilio, localidad, provincia, codigo_postal, telefonos, mail):
        self.apellidos = apellidos
        self.nombres = nombres
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.domicilio = domicilio
        self.localidad = localidad
        self.provincia = provincia
        self.codigo_postal = codigo_postal
        self.telefonos = telefonos
        self.mail = mail

    def __str__(self):
        return f"{self.apellidos},{self.nombres},{self.dni},{self.fecha_nacimiento},{self.domicilio},{self.localidad},{self.provincia},{self.codigo_postal},{self.telefonos},{self.mail}"

    @classmethod
    def from_string(cls, usuario_str):
        campos = usuario_str.strip().split(',')
        return cls(*campos)