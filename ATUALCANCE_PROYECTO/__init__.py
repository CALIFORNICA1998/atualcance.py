class Usuario:
    def _init_(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
        
    def log_in(self):
        pass
    
    def log_out(self):
        pass

class Cliente(Usuario):
    def _init_(self, id, nombre, email, direccion, telefono, puntos):
        super()._init_(id, nombre, email)
        self.direccion = direccion
        self.telefono = telefono
        self.puntos = puntos
        
class Proveedor(Usuario):
    def _init_(self, id, nombre, email, direccion, telefono, productos):
        super()._init_(id, nombre, email)
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos

class Sistema:
    def _init_(self, id_sistema, nombre, version, fecha_creacion):
        self.id_sistema = id_sistema
        self.nombre = nombre
        self.version = version
        self.fecha_creacion = fecha_creacion

class Reserva:
    def _init_(self, id, fecha_reserva, cliente_id):
        self.id = id
        self.fecha_reserva = fecha_reserva
        self.cliente_id = cliente_id

class Comentario:
    def _init_(self, id, texto, cliente_id):
        self.id = id
        self.texto = texto
        self.cliente_id = cliente_id

class Servicio:
    def _init_(self, id, nombre, descripcion, precio, duracion, proveedor_id, fecha_servicio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.duracion = duracion
        self.proveedor_id = proveedor_id
        self.fecha_servicio = fecha_servicio