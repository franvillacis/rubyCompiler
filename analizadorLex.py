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
        'NEWLINE',
        'NUMERO',
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

    def t_STRING(self,t):
        r'\"[^"]*\"'  
        return t

    def t_NUMERO(self,t):
        r'\d+'
        return t
    
    def t_COMMENT(self,t):
        r'\#[^\n]*'
        pass

    def t_error(self,t):
            print("Caracter no reconocido '%s'" % t.value[0])
            t.lexer.skip(1)
    
    def t_NEWLINE(self,t):
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
            if(token.type != 'NEWLINE'):
                tokns.append([token,type,token.value])
        return tokns

archivo_prueba = open('Test.rb','r').read()
analizador = AnalizadorLexico() 
analizador.build()
tokns = analizador.tokenizer(archivo_prueba)
print(tokns)