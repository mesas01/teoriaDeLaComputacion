from antlr4 import *
from gen.LinguaPyLexer import LinguaPyLexer
from gen.LinguaPyParser import LinguaPyParser
from AnalizadorVisitorPersonalizado import AnalizadorVisitorPersonalizado

def main():
    # Asegúrate de especificar la codificación UTF-8 al abrir el archivo
    input_stream = FileStream('pruebasDeLenguaje.lpy', encoding='utf-8')

    lexer = LinguaPyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LinguaPyParser(token_stream)

    tree = parser.programa()

    visitor = AnalizadorVisitorPersonalizado()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
