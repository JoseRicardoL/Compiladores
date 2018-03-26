class Nodo:
    def __init__(self, tipo, numeracion):
        self.tipo = tipo
        self.numeracion = numeracion

    def __str__(self):
        cadenaTipoNodo = ""
        if self.tipo == 1:
            cadenaTipoNodo = " -> "
        elif self.tipo == 3:
            cadenaTipoNodo = " *  "
        else:
            cadenaTipoNodo = "    "
        return '{}{}'.format(cadenaTipoNodo, self.numeracion)
