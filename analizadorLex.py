import ply.lex as lex
import re
import string
import random

class tokenizador(object):

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
    t_keywords=r'true|unless|until|when|false'
    t_nombre= r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_sumar=r'\+'
    t_restar=r'-'
    t_multi=r'\*'
    t_dividir=r'/'