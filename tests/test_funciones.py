import unittest
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
        notas = [0.0, 3.5, 0.0]
        self.assertEqual(maxima_nota(notas), 3.5)

if __name__ == '__main__':
    unittest.main()
