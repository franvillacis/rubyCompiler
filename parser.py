import ply.yacc as yacc
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens

def p_asignar(p):
    'asignar : variable IGUAL expresion'
    p[0] = p[1] + p[3]

def p_variable(p):
    'variable : SYMBOL'
    p [0]= p[1]

def p_expresion(p):
    'expresion : '

parser = yacc.yacc()

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    if not s: continue
    resultado = parser.parse(s)
    print(resultado)
