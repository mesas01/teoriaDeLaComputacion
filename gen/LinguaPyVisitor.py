# Generated from C:/Users/mesas/PycharmProjects/teoria_entrega1/LinguaPy.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LinguaPyParser import LinguaPyParser
else:
    from LinguaPyParser import LinguaPyParser

# This class defines a complete generic visitor for a parse tree produced by LinguaPyParser.

class LinguaPyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LinguaPyParser#programa.
    def visitPrograma(self, ctx:LinguaPyParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#sentencia.
    def visitSentencia(self, ctx:LinguaPyParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#asignacion.
    def visitAsignacion(self, ctx:LinguaPyParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#escritura.
    def visitEscritura(self, ctx:LinguaPyParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#condicion.
    def visitCondicion(self, ctx:LinguaPyParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#ciclo.
    def visitCiclo(self, ctx:LinguaPyParser.CicloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#bloqueSi.
    def visitBloqueSi(self, ctx:LinguaPyParser.BloqueSiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#bloqueSino.
    def visitBloqueSino(self, ctx:LinguaPyParser.BloqueSinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#expresion.
    def visitExpresion(self, ctx:LinguaPyParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#relacional.
    def visitRelacional(self, ctx:LinguaPyParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#logica.
    def visitLogica(self, ctx:LinguaPyParser.LogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#entero.
    def visitEntero(self, ctx:LinguaPyParser.EnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#flotante.
    def visitFlotante(self, ctx:LinguaPyParser.FlotanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#cadena.
    def visitCadena(self, ctx:LinguaPyParser.CadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguaPyParser#booleano.
    def visitBooleano(self, ctx:LinguaPyParser.BooleanoContext):
        return self.visitChildren(ctx)



del LinguaPyParser