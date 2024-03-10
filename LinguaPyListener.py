# Generated from LinguaPy.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LinguaPyParser import LinguaPyParser
else:
    from LinguaPyParser import LinguaPyParser

# This class defines a complete listener for a parse tree produced by LinguaPyParser.
class LinguaPyListener(ParseTreeListener):

    # Enter a parse tree produced by LinguaPyParser#programa.
    def enterPrograma(self, ctx:LinguaPyParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#programa.
    def exitPrograma(self, ctx:LinguaPyParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#sentencia.
    def enterSentencia(self, ctx:LinguaPyParser.SentenciaContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#sentencia.
    def exitSentencia(self, ctx:LinguaPyParser.SentenciaContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#asignacion.
    def enterAsignacion(self, ctx:LinguaPyParser.AsignacionContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#asignacion.
    def exitAsignacion(self, ctx:LinguaPyParser.AsignacionContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#escritura.
    def enterEscritura(self, ctx:LinguaPyParser.EscrituraContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#escritura.
    def exitEscritura(self, ctx:LinguaPyParser.EscrituraContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#condicion.
    def enterCondicion(self, ctx:LinguaPyParser.CondicionContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#condicion.
    def exitCondicion(self, ctx:LinguaPyParser.CondicionContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#ciclo.
    def enterCiclo(self, ctx:LinguaPyParser.CicloContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#ciclo.
    def exitCiclo(self, ctx:LinguaPyParser.CicloContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#expresion.
    def enterExpresion(self, ctx:LinguaPyParser.ExpresionContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#expresion.
    def exitExpresion(self, ctx:LinguaPyParser.ExpresionContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#relacional.
    def enterRelacional(self, ctx:LinguaPyParser.RelacionalContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#relacional.
    def exitRelacional(self, ctx:LinguaPyParser.RelacionalContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#logica.
    def enterLogica(self, ctx:LinguaPyParser.LogicaContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#logica.
    def exitLogica(self, ctx:LinguaPyParser.LogicaContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#entero.
    def enterEntero(self, ctx:LinguaPyParser.EnteroContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#entero.
    def exitEntero(self, ctx:LinguaPyParser.EnteroContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#flotante.
    def enterFlotante(self, ctx:LinguaPyParser.FlotanteContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#flotante.
    def exitFlotante(self, ctx:LinguaPyParser.FlotanteContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#cadena.
    def enterCadena(self, ctx:LinguaPyParser.CadenaContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#cadena.
    def exitCadena(self, ctx:LinguaPyParser.CadenaContext):
        pass


    # Enter a parse tree produced by LinguaPyParser#booleano.
    def enterBooleano(self, ctx:LinguaPyParser.BooleanoContext):
        pass

    # Exit a parse tree produced by LinguaPyParser#booleano.
    def exitBooleano(self, ctx:LinguaPyParser.BooleanoContext):
        pass



del LinguaPyParser