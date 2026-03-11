def notasPerdidas(notas):
    p = sum(1 for nota in notas if nota <3)
    print("Cantidad de notas perdidas:",p)
    return p
def promedio(notas):
    if not notas:
        return 0
    return round(sum(notas) / len(notas), 2)
