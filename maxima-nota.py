def test_maxima_lista_vacia(self):
    self.assertEqual(calcular_maxima([]), 0)

def test_maxima_notas_normales(self):
    self.assertEqual(calcular_maxima([2.5, 4.0, 3.5]), 4.0)

def test_maxima_notas_limite(self):
    self.assertEqual(calcular_maxima([0.0, 5.0]), 5.0)
