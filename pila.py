def pila(lista):
    lista_pila = []
    for i in lista:
        if i == "(":
            lista_pila.append(i)
        elif i == ")":
            if not lista_pila:
                return False
            lista_pila.pop()
    if lista_pila:
        return False
    else:
        return True
