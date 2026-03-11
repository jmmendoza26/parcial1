import unittest
<<<<<<< HEAD
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
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.funciones import promedio

class TestPromedio(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        self.assertEqual(promedio([]), 0)

    def test_promedio_notas_normales(self):
        self.assertEqual(promedio([3.0, 4.0, 5.0]), 4.0)

    def test_promedio_notas_con_cero(self):
        self.assertEqual(promedio([0, 5, 5]), 3.33)

if __name__ == '__main__':
    unittest.main()

=======
import sys
import os

# Agregar src al path para poder importar functions.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.funciones import maxima_nota

class TestMaximaNota(unittest.TestCase):

    def test_maxima_nota_normal(self):
        notas = [3.5, 4.0, 5.0, 2.5, 4.5]
        self.assertEqual(maxima_nota(notas), 5.0)

    def test_maxima_nota_vacio(self):
        notas = []
        self.assertIsNone(maxima_nota(notas))

    def test_maxima_nota_todas_cero(self):
        notas = [0.0, 0.0, 0.0]
        self.assertEqual(maxima_nota(notas), 0.0)

if __name__ == '__main__':
    unittest.main()
>>>>>>> origin/jsmoreno86
