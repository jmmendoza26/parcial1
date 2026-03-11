import unittest
from src.funciones import notasPerdidas


class TestContarNotasPerdidas(unittest.TestCase):

    def test_mezcla_notas(self):
        notas = [4.5, 3.2, 2.8, 1.0, 5.0]
        self.assertEqual(notasPerdidas(notas), 2)

    def test_todas_aprobadas(self):
        notas = [3.0, 3.5, 4.0, 5.0]
        self.assertEqual(notasPerdidas(notas), 0)

    def test_todas_perdidas(self):
        notas = [2.5, 1.0, 2.9]
        self.assertEqual(notasPerdidas(notas), 3)

    def test_lista_vacia(self):
        notas = []
        self.assertEqual(notasPerdidas(notas), 0)

if __name__ == "__main__":
    unittest.main()