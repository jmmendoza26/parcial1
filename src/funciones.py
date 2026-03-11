def notasPerdidas(notas):
    p = sum(1 for nota in notas if nota <3)
    print("Cantidad de notas perdidas:",p)
    return p