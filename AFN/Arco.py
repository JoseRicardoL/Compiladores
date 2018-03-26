class Arco:
    def __init__(self, nodoInicio, nodosDestino):
        self.nodoInicio = nodoInicio
        self.nodosDestino = nodosDestino

    def __str__(self):
        cadenaNodosDestino = ""
        for nodoDestino in self.nodosDestino:
            for elemento in nodoDestino:
                cadenaNodosDestino += str(elemento)
        print(self.nodoInicio, cadenaNodosDestino)
        return ""
