def notasPerdidas(notas):
    return sum(1 for nota in notas if nota <3)