import unittest
from datetime import datetime


from manage import Usuario, Cliente, MetodoPago, Proveedor, Reserva, Comentario, Servicio

class TestUsuario(unittest.TestCase):
    def test_usuario_creation(self):
        user = Usuario(1, "bryan", "bryan@example.com")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.nombre, "bryan")
        self.assertEqual(user.email, "bryan@example.com")



class TestCliente(unittest.TestCase):
    def test_cliente_creation(self):
        cliente = Cliente(1, "Sydney", "Sydney@example.com", "123 Calle 1", "numero")
        self.assertEqual(cliente.id, 1)
        self.assertEqual(cliente.nombre, "Sydney")
        self.assertEqual(cliente.email, "Sydney@example.com")
        self.assertEqual(cliente.direccion, "123 Calle 1")
        self.assertEqual(cliente.telefono, "numero")



class TestMetodoPago(unittest.TestCase):
    def test_metodo_pago(self):
        metodo_pago = MetodoPago("tarjeta")
        self.assertEqual(metodo_pago.metodo, "tarjeta")

    def test_pagar(self):
        metodo_pago = MetodoPago("tarjeta")
        resultado = metodo_pago.pagar(100)
        self.assertIsNone(resultado) 


class TestProveedor(unittest.TestCase):
    def test_proveedor_creation(self):
        proveedor = Proveedor(1, "bryan", "bryan@example.com", "Calle 2", "numero", ["producto1", "producto2"])
        self.assertEqual(proveedor.id, 1)
        self.assertEqual(proveedor.nombre, "bryan")
        self.assertEqual(proveedor.email, "bryan@example.com")
        self.assertEqual(proveedor.direccion, "Calle 2")
        self.assertEqual(proveedor.telefono, "numero")
        self.assertListEqual(proveedor.productos, ["producto1", "producto2"])

    def test_agregar_servicio(self):
        proveedor = Proveedor(1, "bryan", "bryan@example.com", "Calle 2", "numero", ["producto1", "producto2"])
        proveedor.agregar_servicio("servicio1")
        self.assertListEqual(proveedor.servicios_ofrecidos, ["servicio1"])


class TestReserva(unittest.TestCase):
    def test_reserva_creation(self):
        fecha_reserva = datetime.now()
        reserva = Reserva(1, fecha_reserva, 1)
        self.assertEqual(reserva.id, 1)
        self.assertEqual(reserva.fecha_reserva, fecha_reserva)
        self.assertEqual(reserva.cliente_id, 1)


class TestComentario(unittest.TestCase):
    def test_comentario_creation(self):
        comentario = Comentario(1, "Excelente servicio", 1)
        self.assertEqual(comentario.id, 1)
        self.assertEqual(comentario.texto, "Excelente servicio")
        self.assertEqual(comentario.cliente_id, 1)


class TestServicio(unittest.TestCase):
    def test_servicio_creation(self):
        fecha_servicio = datetime.now()
        servicio = Servicio(1, "Servicio A", "Descripción del servicio A", 50, 60, 1, fecha_servicio)
        self.assertEqual(servicio.id, 1)
        self.assertEqual(servicio.nombre, "Servicio A")
        self.assertEqual(servicio.descripcion, "Descripción del servicio A")
        self.assertEqual(servicio.precio, 50)
        self.assertEqual(servicio.duracion, 60)
        self.assertEqual(servicio.proveedor_id, 1)
        self.assertEqual(servicio.fecha_servicio, fecha_servicio)


if __name__ == "__main__":
    unittest.main()
