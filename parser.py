import ply.yacc as yacc
import logging
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens

#Andres Noboa
def p_bloque(p):
    '''bloque : sentencia NEWLINE bloque
              | sentencia'''
    p[0] = p[1]

#Andres Noboa
def p_sentencia(p):
    '''sentencia : estructura_control
                 | expresion'''
    p[0] = p[1]


#Andres Noboa
def p_estructura_control(p):
    '''estructura_control : if
                          | else
                          | elsif
                          | while'''
    p[0] = p[1]

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

#Francisco Villacis
def p_expresion_logic(p):
    '''logica : expresion MAYOR expresion
                      | expresion MENOR expresion
                      | expresion MAYORIGUAL expresion
                      | expresion MENORIGUAL expresion
                      | expresion IGUALIGUAL expresion
                      | expresion NOIGUAL expresion'''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]


#Andres Noboa
def p_expresion_sumar(p):
    'expresion : expresion SUMAR expresion'
    p[0] = p[1] + p[3]

#Andres Noboa
def p_expresion_restar(p):
    'expresion : expresion RESTAR expresion'
    p[0] = p[1] - p[3]

#Andres Noboa
def p_expresion_multiplicar(p):
    'expresion : expresion MULTIPLICAR expresion'
    p[0] = p[1] * p[3]

#Andres Noboa
def p_expresion_dividir(p):
    'expresion : expresion DIVIDIR expresion'
    p[0] = p[1] / p[3]

#Andres Noboa
def p_expresion_factor(p):
    'expresion : factor'
    p[0] = p[1]

#Andres Noboa
def p_factor(p):
    '''factor : INT
              | FLOAT
              | STRING '''
    p[0] = p[1]

#Andres Noboa
def p_error(p):
    print(p)
    print("Ups! tuviste un error.")


parser = yacc.yacc()

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
logger = logging.getLogger()

s = open('test.rb','r').read()
result = parser.parse(s, debug=logger)
