import ply.yacc as yacc
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens

def p_bloque(p):
    '''bloque : sentencia NEWLINE bloque
              | sentencia'''

def p_sentencia(p):
    '''sentencia : estructura_control
                 | expresion'''


def p_estructura_control(p):
    '''estructura_control : if
                          | else
                          | elsif
                          | while'''

def p_if(p):
    '''if : IF PARENIZ logica PARENDER 
          | IF logica THEN expresion'''

def p_elsif(p):
    '''elsif : ELSIF PARENIZ logica PARENDER THEN expresion
             | ELSIF logica THEN expresion'''

def p_else(p):
    'else : ELSE'

def p_while(p):
    '''while : WHILE PARENIZ logica PARENDER THEN expresion
             | WHILE logica NEWLINE bloque'''


def p_logica_mayor(p):
    'logica : SYMBOL MAYOR SYMBOL'

def p_logica_menor(p):
    'logica : SYMBOL MENOR SYMBOL'

def p_logica_mayor_igual(p):
    'logica : SYMBOL MAYORIGUAL SYMBOL'

def p_logica_menor_igual(p):
    'logica : SYMBOL MENORIGUAL SYMBOL'

def p_expresion_sumar(p):
    'expresion : expresion SUMAR expresion'

def p_expresion_restar(p):
    'expresion : expresion RESTAR expresion'

def p_expresion_multiplicar(p):
    'expresion : expresion MULTIPLICAR expresion'

def p_expresion_dividir(p):
    'expresion : expresion DIVIDIR expresion'

def p_expresion_factor(p):
    'expresion : factor'

def p_factor(p):
    '''factor : INT
              | FLOAT
              | STRING '''

def p_error(p):
    print("Ups! tuviste un error.")


parser = yacc.yacc()

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    if not s: continue
    resultado = parser.parse(s)
    print(resultado)