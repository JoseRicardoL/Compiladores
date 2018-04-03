from Expresion import Expresion
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("Expresion",
                    help="Introducir una Expresion regular para poder la\n"
                    "procesar a un automata finito no deterministico y \n"
                    "mostrar su tabla de transiciones")

args = parser.parse_args()

ER = Expresion()

resultado = ER.expresionPostFija(args.Expresion)

evaluacion = ER.evaluacionExpresion(resultado)

fichero = open('fichero.txt', 'w')

for elemento in evaluacion:
    for tabla in elemento.tablaTransiciones:
        fichero.write('{}'.format(tabla))
fichero.close()
