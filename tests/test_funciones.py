import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from funciones import promedio

class TestPromedio(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        self.assertEqual(promedio([]), 0)

    def test_promedio_notas_normales(self):
        self.assertEqual(promedio([3.0, 4.0, 5.0]), 4.0)

    def test_promedio_notas_con_cero(self):
        self.assertAlmostEqual(promedio([0, 5, 5]), 3.333, places=3)

if __name__ == '__main__':
    unittest.main()
