def promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)
