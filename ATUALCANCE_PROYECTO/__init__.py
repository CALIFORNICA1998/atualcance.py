from abc import ABC

class Usuario(ABC):
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

   
    def log_in(self):
        pass

    
    def log_out(self):
        pass

class Cliente(Usuario):
    def __init__(self, id, nombre, email, direccion, telefono):
        super().__init__(id, nombre, email)
        self.direccion = direccion
        self.telefono = telefono
    
    def iniciar_sesion(self):
        print("Sesión iniciada")

    def cerrar_sesion(self):
        print("Sesión terminada")

class MetodoPago (Cliente):
    def __init__(self, metodo):
        self.metodo = metodo
    
    def pagar(self, monto):
        print(f"Procesando pago de {monto} con {self.metodo}")
    

class Proveedor(Usuario):
    def __init__(self, id, nombre, email, direccion, telefono, productos):
        super().__init__(id, nombre, email)
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos
        self.servicios_ofrecidos = []  

    def log_in(self):
        print("sesion iniciada")

    def log_out(self):
        print("sesion terminada")
        
    def agregar_servicio(self, servicio):
        self.servicios_ofrecidos.append(servicio)
        

class Reserva:
    def __init__(self, id, fecha_reserva, cliente_id):
        self.id = id
        self.fecha_reserva = fecha_reserva
        self.cliente_id = cliente_id

class Comentario:
    def __init__(self, id, texto, cliente_id):
        self.id = id
        self.texto = texto
        self.cliente_id = cliente_id

class Servicio:
    def __init__(self, id, nombre, descripcion, precio, duracion, proveedor_id, fecha_servicio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.duracion = duracion
        self.proveedor_id = proveedor_id
        self.fecha_servicio = fecha_servicio
        
    def herramintas(self):
        pass
        
class gasfiteria(Servicio):
    def __init__(self):
        pass
    
    def materiales (self):
        print("herramientas a usar")
        
class pintura(Servicio):
    def __init__(self):
        pass
    
    def materiales (self):
        print("herramientas a usar")
        
class albañeria(Servicio):
    def __init__(self):
        pass
    
    def materiales (self):
        print("herramientas a usar")  
        
class serviciosmecanicos(Servicio):
    def __init__(self):
        pass
    
    def materiales (self):
        print("herramientas a usar")        
        
class ServicioAtencion:
    def __init__(self, servicio: Servicio) -> None:
        self.servicio = servicio
        
    def atencion_al_cliente(self)-> None:
        self.servicio.herramintas()

         