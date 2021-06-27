import ply.lex as lex
import re
import string
import random

class Tokenizador(object):

    tokens = (
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


    def t_string(self,t):
        r'\"[^"]*\"'  
        return t


    def t_comment(self,t):
        r'\#[^\n]*'
        pass

    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)