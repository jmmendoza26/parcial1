def calcular_maxima(notas):
    """
    Función que recibe un arreglo de notas y retorna la nota máxima
    
    Parámetros:
    notas: lista de números (entre 0 y 5)
    
    Retorna:
    - 0 si la lista está vacía
    - La nota máxima si la lista tiene elementos
    """
    if not notas:  # Si la lista está vacía
        return 0
    
    # Encontrar la nota máxima
    maxima = notas[0]  # Suponemos que la primera es la máxima
    
    for nota in notas:
        if nota > maxima:
            maxima = nota
    
    return maxima
