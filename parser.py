import ply.yacc as yacc
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens



def p_expresion_logica(p):
    '''expresion_logica : SYMBOL MAYOR SYMBOL
                        | SYMBOL MENOR SYMBOL
                        | SYMBOL MAYORIGUAL SYMBOL
                        | SYMBOL MENORIGUAL SYMBOL'''
#***************************************Ana Briones****************************************************
def p_expresion_suma(p):
    'expresion : expresion SUMAR expresion'
def p_expresion_resta(p):
    'expresion : expresion RESTAR expresion'
def p_expresion_producto(p):
    'expresion : expresion MULTIPLICAR expresion'
def p_expresion_division(p):
    'expresion : expresion DIVIDIR expresion'                  

def p_sentencia(p):
    '''
    sentencia: imprimir
             | if 
             | while
             | forEach
             | else
             | elsif
             | unless
             | until
             | asignar
             | sentencia sentencia
    '''

def p_imprimir(p):
    'imprimir: puts valorVar '
def p_bloque(p):
    '''bloque : sentencia NEWLINE bloque
              | sentencia'''


def p_asignar(p):
    '''asignar : SYMBOL IGUAL expresion '''



def p_if(p):
    'if : IF logica THEN expresion'

def p_elseif(p):
    'elseif : ELSEIF logica THEN expresion'

def p_variable(p):
    'variable: t_STRING t_IGUAL expresion '
def p_variable_local(p):
    'variable: ARROBA t_STRING t_IGUAL expresion '
def p_variable_global(p):
    'variable: DOLAR t_STRING t_IGUAL expresion '
def p_variable_clase(p):
    'variable: DARROBA t_STRING t_IGUAL expresion '

def p_valorVar(p):
    '''
    valorVar:  t_STRING
             | t_NUMERO
             | t_INT
             | t_FLOAT
             | TRUE
             | FALSE
    '''

def p_while(p):
    '''while : WHILE  condicion DO sentencia END 
             | BEGIN sentencia END WHILE condicion
    
    '''
def p_until(p):
    ''' until: UNTIL condicion DO sentencia END
             |  BEGIN sentencia END UNTIL condicion
    '''


def p_forEach(p):
    '''
    forEach: variable IN expresion DO sentencia END
           | expresion PUNTO EACH DO PIPE variable PIPE sentencia END
    '''


def p_if(p):
    '''
    if: IF condicion THEN sentencia 
      | IF PARENIZ condicion PARENDER THEN sentencia
      | IF condicion THEN sentencia else   
    
    '''
def p_elsif(p):
    '''
    elsif: ELSIF condicion THEN sentencia
        | ELSIF PARENIZ condicion PARENDER THEN sentencia
    '''

def p_else(p):
    '''
    else: ELSE sentencia END
        

    '''
def p_unless(p):
    'unless: UNLESS sentencia'

def p_condicion(p):
    '''
    condicion: expresion comparador expresion 
    '''
def p_comparador(p):
    '''
    comparador: MAYORIGUAL
              | MENORIGUAL
              | MAYOR
              | MENOR
    '''
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
    '''expresion :NUMERO
                 | STRING'''
def p_error(p):
    print("Ups! tuviste un error.")




#¨***************************************************Andres Noboa************************************************
parser = yacc.yacc()

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    if not s: continue
    resultado = parser.parse(s)
    print(resultado)