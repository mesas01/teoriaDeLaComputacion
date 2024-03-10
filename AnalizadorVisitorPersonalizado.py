# AnalizadorVisitorPersonalizado.py
from gen.LinguaPyVisitor import LinguaPyVisitor
from gen.LinguaPyParser import LinguaPyParser

class AnalizadorVisitorPersonalizado(LinguaPyVisitor):
    def __init__(self):
        self.symbolTable = {}
        print("Inicializando tabla de símbolos...")

    def visitPrograma(self, ctx: LinguaPyParser.ProgramaContext):
        print("Visitando programa...")
        return self.visitChildren(ctx)

    def visitSentencia(self, ctx: LinguaPyParser.SentenciaContext):
        print("Visitando sentencia...")
        return self.visitChildren(ctx)

    # Modificación en visitAsignacion para asegurar la correcta actualización de variables
    def visitAsignacion(self, ctx: LinguaPyParser.AsignacionContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        if value is not None:
            self.symbolTable[var_name] = value
            print(f"Variable '{var_name}' actualizada a {value}.")
        else:
            print(f"Error: intento de asignar un valor no válido a '{var_name}'.")
        return value

    def visitCiclo(self, ctx: LinguaPyParser.CicloContext):
        print("Visitando ciclo...")
        while self.visit(ctx.expresion()):
            print(f"Evaluación de expresión en ciclo dio True. Tabla de símbolos: {self.symbolTable}")
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
            print(f"Fin de iteración del ciclo. Tabla de símbolos: {self.symbolTable}")

    def visitEscritura(self, ctx: LinguaPyParser.EscrituraContext):
        value = self.visit(ctx.expresion())
        if isinstance(value, bool):
            value = "verdadero" if value else "falso"
        print(f"Valor a escribir: {value}")
        return value

    def visitExpresion(self, ctx):
        if ctx.getChildCount() == 1:
            # Caso base: literal, identificador o expresión entre paréntesis
            if ctx.entero():
                return self.visitEntero(ctx.entero())
            elif ctx.flotante():
                return self.visitFlotante(ctx.flotante())
            elif ctx.cadena():
                return self.visitCadena(ctx.cadena())
            elif ctx.booleano():
                return self.visitBooleano(ctx.booleano())
            elif ctx.ID() is not None:
                var_name = ctx.ID().getText()
                if var_name in self.symbolTable:
                    return self.symbolTable[var_name]
                else:
                    print(f"Error: Variable '{var_name}' no definida.")
                    return None
        elif ctx.getChildCount() == 2:
            # Operaciones unarias como negación numérica
            op = ctx.getChild(0).getText()
            right = self.visit(ctx.expresion(0))
            if op == '-':
                return -right
            else:
                print(f"Operación unaria '{op}' no soportada.")
                return None
        elif ctx.getChildCount() == 3:
            # Operaciones binarias
            left = self.visit(ctx.expresion(0))
            right = self.visit(ctx.expresion(1))
            op = ctx.getChild(1).getText()
            if op in ['+', '-', '*', '/']:
                return self.performArithmeticOperation(left, right, op)
            elif op in ['>', '<', '>=', '<=', '==', '!=']:
                return self.performRelationalOperation(left, right, op)
            elif op in ['&&', '||']:
                return self.performLogicalOperation(left, right, op)
            else:
                print(f"Operación '{op}' no soportada.")
                return None
        else:
            print("Expresión no reconocida.")
            return None

    def visitBooleano(self, ctx: LinguaPyParser.BooleanoContext):
        return True if ctx.getText() == 'verdadero' else False

    def performArithmeticOperation(self, left, right, op):
        if op == '+':
            # Especialmente manejar la concatenación de cadena con otros tipos
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            else:
                return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                print("Error: División por cero.")
                return None
            return left / right
        else:
            print(f"Error: Operación '{op}' no soportada.")
            return None

    def performRelationalOperation(self, left, right, op):
        if op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '>=':
            return left >= right
        elif op == '<=':
            return left <= right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        return None

    def performLogicalOperation(self, left, right, op):
        if op == '&&':
            return left and right
        elif op == '||':
            return left or right
        return None

    def performUnaryOperation(self, value, op):
        if op == '-':
            return -value
        return value

    def visitEntero(self, ctx: LinguaPyParser.EnteroContext):
        value = int(ctx.getText())
        print(f"Visitando entero: {value}")
        return value

    def visitFlotante(self, ctx: LinguaPyParser.FlotanteContext):
        value = float(ctx.getText())
        print(f"Visitando flotante: {value}")
        return value

    def visitCadena(self, ctx: LinguaPyParser.CadenaContext):
        return ctx.getText().strip('"')

    def visitCondicion(self, ctx: LinguaPyParser.CondicionContext):
        if self.visit(ctx.expresion()):
            print("La condición es verdadera, ejecutando bloque 'si'.")
            self.visit(ctx.bloqueSi())
        elif ctx.bloqueSino() is not None:
            print("La condición es falsa, ejecutando bloque 'sino'.")
            self.visit(ctx.bloqueSino())

    def visitBloqueSi(self, ctx: LinguaPyParser.BloqueSiContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)

    def visitBloqueSino(self, ctx: LinguaPyParser.BloqueSinoContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
