class AFN:
    def __init__(self, listaIndices, tablaTransiciones):
        self.listaIndices = listaIndices
        self.tablaTransiciones = tablaTransiciones

    def __str__(self):
        for indice in self.listaIndices:
            print(indice)
        for transicion in self.tablaTransiciones:
            print(transicion)
        return "fin"

    def buscarNodo(self, nodoInicio):
        for transicion in self.tablaTransiciones:
            if transicion.nodoInicio == nodoInicio:
                return transicion
            else:
                return None
