from AFN import AFN
from Arco import Arco
from Nodo import Nodo


def casoBase(notacion):
    lista_nodos = [Nodo(1, "1"), Nodo(3, "2")]
    return AFN(["Nodos", notacion],
               [Arco(lista_nodos[0], [[lista_nodos[1], notacion]]),
                Arco(lista_nodos[1], [])])


def concatenacion(AFN_1, AFN_2):
    afnConcatenado = AFN(["Nodos"], [])
    transicionAux_1 = []
    transicionAux_2 = []
    i = 0
    for indices in (AFN_1.listaIndices, AFN_2.listaIndices):
        for indice in indices:
            if indice not in AFN_1.listaIndices:
                afnConcatenado.listaIndices.append(indice)
    for transiciones in (AFN_1.tablaTransiciones, AFN_2.tablaTransiciones):
        for transicion in transiciones:
            if transicion not in afnConcatenado.tablaTransiciones:
                if transicion.nodoInicio.tipo == 3 and transicion in AFN_1.tablaTransiciones:
                    transicion.nodoInicio.tipo = 2
                    transicionAux_1 = transicion
                elif transicion.nodoInicio.tipo == 1 and transicion in AFN_2.tablaTransiciones:
                    transicion.nodoInicio.tipo = 2
                    transicionAux_2 = transicion
                else:
                    afnConcatenado.tablaTransiciones.append(transicion)
    for elemento in transicionAux_2.nodosDestino:
        transicionAux_1.nodosDestino.append(elemento)
    afnConcatenado.tablaTransiciones.append(transicionAux_1)
    for transicion in afnConcatenado.tablaTransiciones:
        transicion.nodoInicio.numeracion = i+1
        i += 1
    return afnConcatenado


def union(AFN_1, AFN_2):
    nodoInicio = Nodo(1, "1")
    nodoFin = Nodo(3, "2")
    afnUnido = AFN(["Nodos", "E"], [Arco(nodoInicio, []), Arco(nodoFin, [])])
    for lista in (AFN_1.listaIndices, AFN_2.listaIndices):
        for indice in lista:
            if indice not in afnUnido.listaIndices:
                afnUnido.listaIndices.append(indice)
    for transiciones in (AFN_1.tablaTransiciones, AFN_2.tablaTransiciones):
        for transicion in transiciones:
            if transicion not in afnUnido.tablaTransiciones:
                transicion.nodoInicio.numeracion = len(
                    afnUnido.tablaTransiciones)+1
                if transicion.nodoInicio.tipo == 1:
                    afnUnido.buscarNodo(nodoInicio).nodosDestino.append(
                        [transicion.nodoInicio, "E"])
                    afnUnido.tablaTransiciones.append(transicion)
                elif transicion.nodoInicio.tipo == 3:
                    afnUnido.tablaTransiciones.append(
                        Arco(transicion.nodoInicio, [[nodoFin, "E"]]))
                else:
                    afnUnido.tablaTransiciones.append(transicion)
                transicion.nodoInicio.tipo = 2
    return afnUnido


def cerraduraPositiva(AFN_1):
    nodoInicio = Nodo(1, "1")
    nodoFin = Nodo(3, "2")
    afnCP = AFN(["Nodos", "E"], [Arco(nodoInicio, []), Arco(nodoFin, [])])
    for indice in AFN_1.listaIndices:
            if indice not in afnCP.listaIndices:
                afnCP.listaIndices.append(indice)
    for transicion in AFN_1.tablaTransiciones:
        transicion.nodoInicio.numeracion = len(afnCP.tablaTransiciones)+1
        if transicion.nodoInicio.tipo == 3:
            if transicion not in afnCP.tablaTransiciones:
                for transicion_2 in AFN_1.tablaTransiciones:
                    if transicion_2.nodoInicio.tipo == 1:
                        afnCP.buscarNodo(nodoInicio).nodosDestino.append(
                                [transicion_2.nodoInicio, "E"])
                        afnCP.tablaTransiciones.append(Arco(
                            transicion.nodoInicio,
                            [[nodoFin, "E"], [transicion_2.nodoInicio, "E"]]))
                        transicion_2.nodoInicio.tipo = 2
                        transicion.nodoInicio.tipo = 2
                        if transicion_2 not in afnCP.tablaTransiciones:
                            afnCP.tablaTransiciones.append(transicion_2)
        else:
            afnCP.tablaTransiciones.append(transicion)
    return afnCP


def cerraduraKleene(AFN_1):
    afnCK = cerraduraPositiva(AFN_1)
    for transicion_1 in afnCK.tablaTransiciones:
        for transicion_2 in afnCK.tablaTransiciones:
            if transicion_1.nodoInicio.tipo == 1:
                if transicion_2.nodoInicio.tipo == 3:
                    transicion_1.nodosDestino.append(
                        [transicion_2.nodoInicio, "E"])
    return afnCK
