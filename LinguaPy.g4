// Definición de la gramática para LinguaPy
grammar LinguaPy;

// Definición del programa principal: una serie de sentencias seguidas por el fin de archivo (EOF)
programa : sentencia* EOF;

// Definición de tipos de sentencias permitidas en el lenguaje
sentencia : asignacion
          | escritura
          | condicion
          | ciclo
          ;

// Reglas para las diferentes sentencias
asignacion : ID '=' expresion ';'; // Asigna el valor de una expresión a un identificador
escritura  : 'escribir' '(' expresion ')' ';'; // Imprime el valor de una expresión
condicion  : 'si' '(' expresion ')' bloqueSi ( 'sino' bloqueSino )?;
//condicion  : 'si' '(' expresion ')' '{' sentencia* '}' ('sino' '{' sentencia* '}')?; // Estructura condicional con bloque opcional "sino"
ciclo      : 'mientras' '(' expresion ')' '{' sentencia* '}'; // Ciclo mientras
// Subreglas para bloques de condición
bloqueSi   : '{' sentencia* '}';
bloqueSino : '{' sentencia* '}';

// Definición de expresiones
expresion  : expresion ('*' | '/' | '%') expresion // Operaciones matemáticas: multiplicación, división, módulo
           | expresion ('+' | '-') expresion // Suma y resta, también sirve para concatenación de cadenas
           | expresion ('^') expresion // Potenciación
           | '(' expresion ')' // Agrupación de expresiones con paréntesis para alterar precedencia
           | '-' expresion // Negación de una expresión numérica
           | ID // Identificador
           | entero
           | flotante
           | cadena // Cadena de texto
           | booleano // Valor booleano (verdadero o falso)
           | expresion relacional expresion // Operaciones relacionales
           | expresion logica expresion // Operaciones lógicas
           ;

// Operadores relacionales y lógicos
relacional : '>' | '<' | '>=' | '<=' | '==' | '!='; // Operadores relacionales
logica     : '&&' | '||'; // Operadores lógicos (AND, OR)

// Tokens básicos
BOOLEANO  : 'verdadero' | 'falso'; // Booleano: verdadero o falso
ID        : [a-zA-Z][a-zA-Z0-9]*; // Identificador: debe comenzar con letra y puede contener letras y números
ENTERO    : DIGITO+; // Número entero
FLOTANTE  : DIGITO+ '.' DIGITO+; // Número flotante
CADENA    : '"' (ESC_SEQ | ~["\\])* '"'; // Cadena de texto: caracteres entre comillas dobles

DIGITO    : [0-9]; // Dígito numérico
fragment ESC_SEQ : '\\' [btnr"\\]; // Secuencias de escape en cadenas (e.g., \n, \t)

// Reglas para número, cadena y booleano
//numero    : NUMERO; // Número
entero    : ENTERO;
flotante  : FLOTANTE;
cadena    : CADENA; // Cadena
booleano  : BOOLEANO; // Booleano

// Ignorar espacios en blanco y saltos de línea
WS : [ \t\r\n]+ -> skip;

// Comentarios: línea y multilínea
COMENTARIO_LINEA     : '//' ~[\r\n]* -> skip; // Comentario de una sola línea
COMENTARIO_MULTILINEA: '/*' .*? '*/' -> skip; // Comentario de múltiples líneas