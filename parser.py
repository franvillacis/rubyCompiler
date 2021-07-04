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
                 | logica
                 | asignar
                 | imprimir 
                 | expresion'''
    p[0] = p[1]


#Andres Noboa
def p_estructura_control(p):
    '''estructura_control : if
                          | else
                          | elsif
                          | while'''
    p[0] = p[1]

#Ana Briones
def p_if(p):
  ''' if  : IF PARENIZ logica PARENDER THEN expresion
          | IF logica THEN expresion'''

#Ana Briones        

def p_elsif(p):
    '''elsif : ELSIF PARENIZ logica PARENDER THEN expresion
             | ELSIF logica THEN expresion'''
#Ana Briones
def p_else(p):
    '''else : ELSE expresion END
            | ELSE NEWLINE bloque END
    '''
#ana Briones
def p_while(p):
    '''while : WHILE PARENIZ logica PARENDER DO expresion END
             | WHILE logica NEWLINE DO expresion END
             | WHILE logica NEWLINE DO bloque END'''

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

#Ana Briones
def p_declarador(p): 
    '''declarador : ARROBA
                | DARROBA'''



#Ana Briones
def p_imprimir(p):
    'imprimir: PUTS valor ' 
    print(p[2])

#Ana Briones
def p_asignar(p):
   'asignar : VARIABLE IGUAL expresion '

#Ana Briones
def p_asignar(p):
   'asignar : declarador VARIABLE IGUAL expresion '


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
def p_expresion_valor(p):
    'expresion : valor'
    p[0] = p[1]




#Andres Noboa
def p_valor(p):
    '''valor : INT
             | FLOAT
    '''
    p[0] = p[1]
#Ana Briones
def p_valor_var(p):
    '''valor : VARIABLE'''

#Ana Briones
def p_valor(p): 
    '''valor : STRING'''
    p[0] = p[1]
#Ana Briones
def p_valor_bool(p): 
    '''valor : TRUE
            | FALSE'''
    if p[1] == 'true':
        p[0] = True
    else:
        p[0] = False

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

while True:
    try:
         s = input('>>')
    except EOFError:
        break
    if not s: continue
    resultado = parser.parse(s)
    print(resultado)

