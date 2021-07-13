import ply.yacc as yacc
import logging
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens

#Andres Noboa
def p_bloque(p):
    '''bloque : sentencia NEWLINE bloque
              | sentencia'''
    length = len(p)
    if length > 3:
        p[0] = p[1] + p [2] + p[0]
    else:
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
                          | unless
                          | until
                          | while'''
    p[0] = p[1]

#Ana Briones
def p_if(p):
    ''' if  : IF PARENIZ logica PARENDER THEN sentencia
            | IF logica THEN sentencia'''
    if p[2] == "(":
        if p[3]:
            p[0]=p[6]
    else:
        if p[2]:
            p[0]=p[4]



#Ana Briones
def p_unless(p):
    'unless : UNLESS sentencia'


#Ana Briones        

def p_elsif(p):
    '''elsif : ELSIF PARENIZ logica PARENDER THEN sentencia
             | ELSIF logica THEN sentencia'''
#Ana Briones
def p_else(p):
    '''else : ELSE sentencia END
            | ELSE NEWLINE bloque END
    '''
#ana Briones
def p_while(p):
    '''while : WHILE PARENIZ logica PARENDER DO sentencia END
             | WHILE logica NEWLINE DO sentencia END
             | WHILE logica NEWLINE DO bloque END'''
    
    if p[2] == "(":
        while p[3]:
            print(p[6])
    else:
        while p[2]:
            print(p[5])


#Ana
def p_until(p):
    ' until : UNTIL logica DO sentencia END '

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
def p_imprimir(p):
    'imprimir : PUTS valor'
    p[0]=(p[2])

#Andres Noboa & Ana Briones
def p_asignar(p):
   'asignar : ID IGUAL expresion '
   p[0] = p[1] = p[3]

#Ana Briones & Andres Noboa
def p_asignar_declarador(p):
   'asignar : variable IGUAL valor '
   p[0] = p[1] = p[3]

#Andres Noboa
def p_variable(p):
    'variable : declarador ID'
    p[0] = p[1] + p[2]

#Ana Briones & Andres Noboa
def p_declarador(p): 
    '''declarador : ARROBA
                  | DARROBA'''
    p[0] = p[1]

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
             | ID
             | STRING
    '''
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
    resultado = parser.parse(s,debug=logger)
    print(resultado)

