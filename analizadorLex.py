import ply.lex as lex
import re
import string
import random

class AnalizadorLexico():

    PALABRAS_RESERVADAS = {
        'true':'TRUE',
        'false':'FALSE',
        'break':'BREAK',
        'until':'UNTIL',
        'when':'WHEN',
        'unless':'UNLESS',
        'begin':'BEGIN',
        'end':'END',
        'case':'CASE',
        'class':'CLASS',
        'def':'DEF',
        'defined':'DEFINE',
        'do':'DO',
        'else':'ELSE',
        'elseif':'ELSEIF',
        'end':'END',
        'ensure':'ensure',
        'for':'FOR',
        'if':'IF',
        'in':'IN',
        'module':'MODULE',
        'next':'NEXT',
        'nil':'NIL',
        'not':'NOT',
        'or':'OR',
        'redo':'REDO',
        'rescue':'RESCUE',
        'retry':'RETRY',
        'return':'RETURN',
        'self':'SELF',
        'super':'SUPER',
        'then':'THEN',
        'undef':'UNDEF',
        'yield':'YIELD',
        'while':'WHILE'
    }

    tokens = (
<<<<<<< HEAD
        'CORCHETEIZ', 
        'CORCHETEDER',
        'LLAVEIZ',
        'LLAVEDER',
        'COMILLAS',
        'DOLAR',
        'COMA',
        'PIPE',
        'MAYOR',
        'PARENIZ',
        'PARENDER',
        'IGUAL',
        'CONCATENAR',
        'INTERVALO',
        'IGNORAR',
        'MENOR',
        'NOMBRE',
        'SUMAR',
        'RESTAR',
        'MULTIPLICAR',
        'DIVIDIR',
        'MAYORIGUAL',
        'MENORIGUAL',
    ) + tuple(PALABRAS_RESERVADAS.values())

    #operadores - true/false - caracteres alfanumericos- simbolos
    t_CORCHETEIZ=r'\['
    t_CORCHETEDER=r'\]'
    t_LLAVEIZ=r'\{'
    t_LLAVEDER=r'\}'
    t_COMILLAS=r'\"'
    t_DOLAR=r'\$'
    t_COMA=r'\,'
    t_PIPE=r'\|'
    t_MAYOR=r'\>'
    t_PARENIZ=r'\('
    t_PARENDER=r'\)'
    t_IGUAL=r'='
    t_CONCATENAR=r'<<'
    t_INTERVALO=r'\.\.'
    t_IGNORAR='[ \t]'
    t_MENOR=r'\<'
    t_NOMBRE= r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_SUMAR=r'\+'
    t_RESTAR=r'-'
    t_MULTIPLICAR=r'\*'
    t_DIVIDIR=r'/'
    t_MAYORIGUAL=r'\>='
    t_MENORIGUAL=r'\<='

    t_ignore = ' \t'
=======
        'corcheteIz', 
        'corcheteDer',
        'llaveIz',
        'llaveDer',
        'comillas',
        'dolar',
        'coma',
        'pipe',
        'mayor',
        'parenIz',
        'parenDer',
        'igual',
        'concatenar',
        'intervalo',
        'ignorar',
        'menor',
        'keywords',
        'nombre',
        'sumar',
        'restar',
        'multi',
        'dividir',
        'mayorIgual',
        'menorIgual',
        'true',
        'false',
        'break',
        'until',
        'when',
        'unless',
        'begin',
        'end',
        'case',
        'class',
        'def',
        'defined',
        'do',
        'else',
        'elseif',
        'end',
        'ensure',
        'for',
        'if',
        'in',
        'module',
        'next',
        'nil',
        'not',
        'or',
        'redo',
        'rescue',
        'retry', 
        'return',
        'self',
        'super',
        'then', 
        'undef',
        'yield',
        'while',
    )

	#operadores - true/false - caracteres alfanumericos- simbolos
    t_corcheteIz=r'\['
    t_corcheteDer=r'\]'
    t_llaveIz=r'\{'
    t_llaveDer=r'\}'
    t_comillas=r'\"'
    t_dolar=r'\$'
    t_coma=r'\,'
    t_pipe=r'\|'
    t_mayor=r'\>'
    t_parenIz=r'\('
    t_parenDer=r'\)'
    t_igual=r'='
    t_concatenar=r'<<'
    t_intervalo=r'\.\.'
    t_ignorar='[ \t]'
    t_menor=r'\<'
    t_keywords=r'true|false|break|until|when|unless|begin|end|case|class|def|defined|do|else|elseif|end|ensure|for|if|in|module|next|nil|not|or|redo|rescue|retry|return|self|super|then|undef|yield|while'    
    t_nombre= r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_sumar=r'\+'
    t_restar=r'-'
    t_multi=r'\*'
    t_dividir=r'/'
    t_mayorIgual=r'\>='
    t_menorIgual=r'\<='


    def t_elsif(self,t):
        r'elsif'
        return t

    def t_while(self,t):
        r'while'
        return t
    
    def t_begin(self,t):
        r'begin'
        return t
    
    def t_break(self,t):
        r'break'
        return t
    
    def t_until(self,t):
        r'until'
        return t
    
    def t_when(self,t):
        r'when'
        return t
    
    def t_unless(self,t):
        r'unless'
        return t

    def t_begin(self,t):
        r'begin'
        return t

    def t_case(self,t):
        r'case'
        return t

    def t_class(self,t):
        r'class'
        return t

    def t_def(self,t):
        r'def'
        return t

    def t_defined(self,t):
        r'defined'
        return t

    def t_else(self,t):
        r'else'
        return t

    def t_elseif(self,t):
        r'elseif'
        return t

    def t_ensure(self,t):
        r'ensure'
        return t

    def t_module(self,t):
        r'module'
        return t
    
    def t_end(self,t):
        r'end'
        return t
    
    def t_for(self,t):
        r'for'
        return t
    
    def t_if(self,t):
        r'if'
        return t
    
    def t_true(self,t):
        r'true'
        return t
    
    def t_false(self,t):
        r'false'
        return t
    
    def t_return(self,t):
        r'return'
        return t
    
    def t_then_tok(self,t):
        r'then'
        return t
    
    def t_in(self,t):
        r'in'
        return t
    
    def t_do(self,t):
        r'do'
        return t
    
    def t_logic(self,t):
        r'or|and'
        return t
    
    def t_logicnot(self,t):
        r'not'
        return t
    
    def t_number(self,t):
        r'\d+'
        t.value = int(t.value)    
        return t

    def t_builtinmethod(self,t):
        r'Array|Float|Integer|String|at_exit|autoload|binding|caller|catch|chop|chop!|chomp|chomp!|eval|exec|exit|exit!|fail|fork|format|gets|global_variables|gsub|gsub!|iterator?|lambda|load|local_variables|loop|open|print|printf|proc|putc|puts|raise|rand|readline|readlines|require|select|sleep|split|sprintf|srand|sub|sub!|syscall|system|test|trace_var|trap|untrace_var' #for built in functions
        return t

>>>>>>> 64317353500b412f1d32c3f7212d0e3948e6ad98

    def t_string(self,t):
        r'\"[^"]*\"'  
        return t


    def t_comment(self,t):
        r'\#[^\n]*'
        pass

    def t_error(self,t):
            print("Caracter no reconocido '%s'" % t.value[0])
            t.lexer.skip(1)
    
    def t_newline(self,t):
	    r'\n+'
	    t.lexer.lineno += len(t.value)
	    return t
    
    def build(self, **kwargs):
        self.lexer=lex.lex(module=self,**kwargs)
    
    def tokenizer(self,data):
        tokns=[]
        self.lexer.input(data)
        while(True):
            token=self.lexer.token()
            if not token:
                break
            if(token.type != 'newline'):
                tokns.append([token,type,token.value])
        return tokns

archivo_prueba = open('TEST.tx','r').read()
analizador = AnalizadorLexico() 
analizador.build()
tokns = analizador.tokenizer()
print(tokns)
