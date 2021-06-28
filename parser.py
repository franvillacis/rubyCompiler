import ply.yacc as yacc
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens


def p_sentencia(p):
    '''sentencia : estructura_control
                 | asignar'''

def p_asignar(p):
    '''asignar : SYMBOL IGUAL NUMERO
               | SYMBOL IGUAL STRING'''

def p_estructura_control(p):
    '''estructura_control : if
                           | elseif
                           | else
                           | while'''

def p_if(p):
    'if : IF PARENIZ logica PARENDER'

def p_elseif(p):
    'elseif : ELSEIF PARENIZ logica PARENDER'

def p_else(p):
    'else : ELSE'

def p_while(p):
    'while : WHILE PARENIZ logica PARENDER'

def p_logica(p):
    '''logica : SYMBOL MAYOR SYMBOL
                    | SYMBOL MENOR SYMBOL
                    | SYMBOL MAYORIGUAL SYMBOL
                    | SYMBOL MENORIGUAL SYMBOL'''

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


