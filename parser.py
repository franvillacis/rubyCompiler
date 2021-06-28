import ply.yacc as yacc
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens

def p_bloque(p):
    '''bloque : sentencia NEWLINE bloque
              | sentencia'''

def p_sentencia(p):
    '''sentencia : estructura_control
                 | asignar'''

def p_asignar(p):
    '''asignar : SYMBOL IGUAL expresion '''

def p_estructura_control(p):
    '''estructura_control : if
                           | elseif
                           | else
                           | while'''

def p_if(p):
    'if : IF logica THEN expresion'

def p_elseif(p):
    'elseif : ELSEIF logica THEN expresion'

def p_else(p):
    'else : ELSE'

def p_while(p):
    'while : WHILE logica NEWLINE bloque'

def p_logica(p):
    '''logica : SYMBOL MAYOR SYMBOL
                    | SYMBOL MENOR SYMBOL
                    | SYMBOL MAYORIGUAL SYMBOL
                    | SYMBOL MENORIGUAL SYMBOL'''
def p_expresion(p):
    '''expresion : expresion SUMAR expresion
                 | expresion RESTAR expresion
                 | expresion MULTIPLICAR expresion
                 | expresion DIVIDIR expresion
                 | termino '''

def p_termino(p):
    '''termino : NUMERO
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


