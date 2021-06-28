import ply.yacc as yacc
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens

def p_if(p):
    'if : IF PARENIZ expresion PARENDER'

def p_expresion_logica(p):
    '''expresion : SYMBOL MAYOR SYMBOL
                    | SYMBOL MENOR SYMBOL
                    | SYMBOL MAYORIGUAL SYMBOL
                    | SYMBOL MENORIGUAL SYMBOL'''


parser = yacc.yacc()

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    if not s: continue
    resultado = parser.parse(s)
    print(resultado)

