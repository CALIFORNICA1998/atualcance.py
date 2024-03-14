from typing import List, Tuple

class Usuario:
    def __init__(self, id: int, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email

class Cliente(Usuario):
    def __init__(self, id: int, nombre: str, email: str, direccion: str, telefono: str):
        super().__init__(id, nombre, email)
        self.direccion = direccion
        self.telefono = telefono

class MetodoPago:
    def __init__(self, metodo: str):
        self.metodo = metodo
    
    def pagar(self, monto: float):
        print(f"Procesando pago de {monto} con {self.metodo}")

class Proveedor(Usuario):
    def __init__(self, id: int, nombre: str, email: str, direccion: str, telefono: str, productos: List[str]):
        super().__init__(id, nombre, email)
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos
        self.servicios_ofrecidos = []  

    def agregar_servicio(self, servicio: str):
        self.servicios_ofrecidos.append(servicio)

    def obtener_nombre_productos(self) -> str:
        return ", ".join(self.productos)

class Reserva:
    def __init__(self, id: int, fecha_reserva: str, cliente_id: int):
        self.id = id
        self.fecha_reserva = fecha_reserva
        self.cliente_id = cliente_id

class Comentario:
    def __init__(self, id: int, texto: str, cliente_id: int):
        self.id = id
        self.texto = texto
        self.cliente_id = cliente_id

class Servicio:
    def __init__(self, id: int, nombre: str, descripcion: str, precio: float, duracion: int, proveedor_id: int, fecha_servicio: str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.duracion = duracion
        self.proveedor_id = proveedor_id
        self.fecha_servicio = fecha_servicio