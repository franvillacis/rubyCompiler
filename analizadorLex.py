import ply.lex as lex


class AnalizadorLexico():
    ''' Clase que se encarga de hacer las deficiones de los tokens y palabras reservadas'''

    # Palabras Reservadas para Ruby
    PALABRAS_RESERVADAS = {
        'true': 'TRUE',
        'false': 'FALSE',
        'until': 'UNTIL',
        'unless': 'UNLESS',
        'end': 'END',
        #'def': 'DEF',
        'do': 'DO',
        'else': 'ELSE',
        'elsif': 'ELSIF',
        'for': 'FOR',
        'if': 'IF',
        'in': 'IN',
        #'not': 'NOT',
        #'or': 'OR',
        #'return': 'RETURN',
        'then': 'THEN',
        'while': 'WHILE',
        'puts' : 'PUTS'

    }

    # Tokens a utilizar
    tokens = (
                 'CORCHETEIZ',
                 'CORCHETEDER',
                 'LLAVEIZ',
                 'LLAVEDER',
                 #'COMILLAS',
                 #'DOLAR',
                 'COMA',
                 #'PIPE',
                 'MAYOR',
                 'PARENIZ',
                 'PARENDER',
                 'IGUAL',
                 #'CONCATENAR',
                 'INTERVALO',
                 #'IGNORAR',
                 'MENOR',
                 'ID',
                 'SUMAR',
                 'RESTAR',
                 'MULTIPLICAR',
                 'DIVIDIR',
                 'MAYORIGUAL',
                 'MENORIGUAL',
                 'IGUALIGUAL',
                 'NOIGUAL',
                 'NEWLINE',
                 #'PUNTO',
                 'ARROBA',
                 'DARROBA',
                 'STRING',
                 'INT',
                 'FLOAT',
                 'HASHROCKET',
             ) + tuple(PALABRAS_RESERVADAS.values())

    #operadores - true/false - caracteres alfanumericos- simbolos
    t_CORCHETEIZ=r'\['
    t_CORCHETEDER=r'\]'
    t_LLAVEIZ=r'\{'
    t_LLAVEDER=r'\}'
    #t_COMILLAS=r'\"'
    #t_DOLAR=r'\$'
    t_COMA=r'\,'
    #t_PIPE=r'\|'
    t_MAYOR = r'>'
    t_PARENIZ=r'\('
    t_PARENDER=r'\)'
    t_IGUAL=r'='
    #t_CONCATENAR=r'<<'
    t_INTERVALO=r'\.\.'
    t_MENOR=r'<'
    t_SUMAR=r'\+'
    t_RESTAR=r'-'
    t_MULTIPLICAR=r'\*'
    t_DIVIDIR=r'/'
    t_MAYORIGUAL=r'>='
    t_MENORIGUAL=r'<='
    t_IGUALIGUAL = r'=='
    t_NOIGUAL = r'!='
    #t_PUNTO=r'\.'
    t_ARROBA=r'@' 
    t_DARROBA=r'@@'
    t_HASHROCKET= r'=>'
    t_ignore = ' \t'

    # definir con expresiones
    def t_END(self,t):
        r'\n'
        pass

    def t_COMMENT(self, t):
        r'\#[^\n]*'
        pass

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.PALABRAS_RESERVADAS.get(t.value, 'ID')
        return t

    def t_INT(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    def t_FLOAT(self, t):
        r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$'
        t.value = float(t.value)
        return t

    def t_STRING(self, t):
        r'"[^".]*"'
        return t

    def t_error(self,t):
            print("Caracter no reconocido '%s'" % t.value[0])
            self.error = str(t.value[0])
            t.lexer.skip(1)
    
    def t_NEWLINE(self,t):
	    r'\n+'
	    t.lexer.lineno += len(t.value)
	    return t
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def tokenizer(self, data):
        tokns = []
        self.lexer.input(data)
        while (True):
            token = self.lexer.token()
            if not token:
                break
            if (token.type != 'NEWLINE'):
                tokns.append([token, type, token.value])
        return tokns



# Test del archivo de prueba de Ruby
error = ""
archivo_prueba = open('test.rb', 'r').read()
analizador = AnalizadorLexico()
analizador.build()
tokns = analizador.tokenizer(archivo_prueba)
if(len(tokns) > 0):
    print('Los tokens son validos!')