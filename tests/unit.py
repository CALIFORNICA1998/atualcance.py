import unittest
from unittest.mock import patch
from io import StringIO

from manage import Usuario, Cliente, MetodoPago, Proveedor, Reserva, Comentario, Servicio

class TestUsuario(unittest.TestCase):
    def test_log_in(self):
        usuario = Usuario(1, "Usuario", "usuario@example.com")
        self.assertIsNone(usuario.log_in())

    def test_log_out(self):
        usuario = Usuario(1, "Usuario", "usuario@example.com")
        self.assertIsNone(usuario.log_out())

class TestCliente(unittest.TestCase):
    def test_iniciar_sesion(self):
        cliente = Cliente(1, "Cliente", "cliente@example.com", "Dirección", "123456789")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cliente.iniciar_sesion()
            self.assertEqual(fake_out.getvalue().strip(), "Sesión iniciada")

    def test_cerrar_sesion(self):
        cliente = Cliente(1, "Cliente", "cliente@example.com", "Dirección", "123456789")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cliente.cerrar_sesion()
            self.assertEqual(fake_out.getvalue().strip(), "Sesión terminada")

class TestMetodoPago(unittest.TestCase):
    def test_pagar(self):
        metodo_pago = MetodoPago("Tarjeta")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            metodo_pago.pagar(100)
            self.assertEqual(fake_out.getvalue().strip(), "Procesando pago de 100 con Tarjeta")

class TestProveedor(unittest.TestCase):
    def test_agregar_servicio(self):
        proveedor = Proveedor(1, "Proveedor", "proveedor@example.com", "Dirección", "123456789", [])
        proveedor.agregar_servicio("Mantenimiento")
        self.assertIn("Mantenimiento", proveedor.servicios_ofrecidos)

class TestReserva(unittest.TestCase):
    def test_init(self):
        reserva = Reserva(1, "2024-03-10", 1)
        self.assertEqual(reserva.id, 1)
        self.assertEqual(reserva.fecha_reserva, "2024-03-10")
        self.assertEqual(reserva.cliente_id, 1)

class TestComentario(unittest.TestCase):
    def test_init(self):
        comentario = Comentario(1, "Excelente servicio", 1)
        self.assertEqual(comentario.id, 1)
        self.assertEqual(comentario.texto, "Excelente servicio")
        self.assertEqual(comentario.cliente_id, 1)

class TestServicio(unittest.TestCase):
    def test_init(self):
        servicio = Servicio(1, "gasfiteria", "Servicio de gasfiteria a domicilio", 50, 1, 1, "2024-03-11")
        self.assertEqual(servicio.id, 1)
        self.assertEqual(servicio.nombre, "gasfiteria")
        self.assertEqual(servicio.descripcion, "Servicio de gasfiteria a domicilio")
        self.assertEqual(servicio.precio, 50)
        self.assertEqual(servicio.duracion, 1)
        self.assertEqual(servicio.proveedor_id, 1)
        self.assertEqual(servicio.fecha_servicio, "2024-03-10")



if __name__ == "__main__":
    unittest.main()
