<<<<<<< HEAD
def notasPerdidas(notas):
    p = sum(1 for nota in notas if nota <3)
    print("Cantidad de notas perdidas:",p)
    return p
def promedio(notas):
    if not notas:
        return 0
    return round(sum(notas) / len(notas), 2)
=======
def maxima_nota(notas):
    """
    Retorna la máxima nota de un arreglo.
    Si el arreglo está vacío, retorna None.
    Si alguna nota está fuera de rango (0-5), lanza una excepción.
    """
    if not notas:
        return None
    
    for nota in notas:
        if nota < 0 or nota > 5:
            raise ValueError(f"Nota {nota} está fuera del rango permitido (0-5)")
    
    return max(notas)
>>>>>>> origin/jsmoreno86
