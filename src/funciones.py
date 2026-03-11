def promedio(notas):
    if not notas:
        return 0
    return round(sum(notas) / len(notas), 2)
