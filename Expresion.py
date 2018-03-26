from Plantillas import (casoBase, cerraduraKleene,
                        cerraduraPositiva, concatenacion, union)
from copy import deepcopy


class Expresion:
    def __init__(self):
        self.pilaOperadores = []
        self.pilaPosfija = []
        self.pExpresion = {'(': 5, '*': 4, '+': 3, '.': 2, '|': 1, ')': 0}
        self.pPila = {'(': 0, '*': 4, '+': 3, '.': 2, '|': 1, ')': 0}
        self.tipo = {'(': 0, '*': 1, '+': 1, '.': 2, '|': 2, ')': 3}

    def expresionPostFija(self, exPrefija):
        listaExPrefija = self.completarListaExPrefija(list(exPrefija))
        for elemento in listaExPrefija:
            if elemento in self.pExpresion:
                if self.pilaOperadores == []:
                    self.pilaOperadores.append(elemento)
                elif elemento == ')':
                    self.vaciarParentesis(elemento)
                else:
                    self.jerarquia(elemento)
            else:
                self.pilaPosfija.append(elemento)
        self.vaciarPilaOp()
        return self.pilaPosfija

    def jerarquia(self, operador):
        if self.pilaOperadores == []:
            self.pilaOperadores.append(operador)
        elif self.pExpresion[operador] > self.pPila[self.pilaOperadores[-1]]:
            self.pilaOperadores.append(operador)
        else:
            self.pilaPosfija.append(self.pilaOperadores[-1])
            self.pilaOperadores.pop()
            self.jerarquia(operador)

    def vaciarParentesis(self, operador):
        if self.pExpresion[operador] != self.pPila[self.pilaOperadores[-1]]:
            self.pilaPosfija.append(self.pilaOperadores[-1])
            self.pilaOperadores.pop()
            self.vaciarParentesis(operador)
        else:
            self.pilaOperadores.pop()

    def vaciarPilaOp(self):
        if self.pilaOperadores != []:
            self.pilaPosfija.append(self.pilaOperadores[-1])
            self.pilaOperadores.pop()
            self.vaciarPilaOp()

    def completarListaExPrefija(self, listaExPrefija):
        lepCom = []
        for elemento in listaExPrefija:
            if lepCom != []:
                if elemento in self.pExpresion:
                    if lepCom[-1] in self.pExpresion:
                        if self.pPila[elemento] > self.pPila[lepCom[-1]]:
                            if self.tipo[elemento] < self.tipo[lepCom[-1]]:
                                if self.tipo[elemento] != 1:
                                    lepCom.append('.')
                        elif self.tipo[elemento] < self.tipo[lepCom[-1]]:
                            if self.tipo[elemento] == 0:
                                lepCom.append('.')
                else:
                    if lepCom[-1] not in self.pExpresion:
                        lepCom.append('.')
                    else:
                        if self.tipo[lepCom[-1]] in [1, 3]:
                            lepCom.append('.')
            lepCom.append(elemento)
        return lepCom

    def evaluacionExpresion(self, Expresion):
        expresionAFN = []
        pilaAFN = []
        for elemento in Expresion:
            if elemento in self.tipo:
                expresionAFN.append(elemento)
            else:
                expresionAFN.append(casoBase(elemento))
        for elemento in expresionAFN:
            if elemento in self.tipo:
                if self.tipo[elemento] == 1:
                    op_1 = pilaAFN.pop()
                    if elemento == "*":
                        pilaAFN.append(cerraduraKleene(deepcopy(op_1)))
                    elif elemento == "+":
                        pilaAFN.append(cerraduraPositiva(deepcopy(op_1)))
                elif self.tipo[elemento] == 2:
                    op_2 = pilaAFN.pop()
                    op_1 = pilaAFN.pop()
                    if elemento == ".":
                        pilaAFN.append(concatenacion(deepcopy(op_1),
                                                     deepcopy(op_2)))
                    elif elemento == "|":
                        pilaAFN.append(union(deepcopy(op_1),
                                             deepcopy(op_2)))
            else:
                pilaAFN.append(elemento)
        return pilaAFN
