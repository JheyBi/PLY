
import ply.lex as lex
from lexDella import tokens



def p_prog(p):
    '''prog : line X'''
    print("Entrou no prog")
    p[0] = p[1]

def p_X(p):
    '''X : EOF
         | prog'''
    print("Entrou no X")
    p[0] = p[1]

def p_line(p):
    '''line : stmt EOL'''
    print("Entrou no line")
    p[0] = p[1]

def p_stmt(p):
    '''stmt : in
            | out
            | atrib'''
    print("Entrou no stmt")
    p[0] = p[1]

def p_in(p):
    '''in : INPUT VAR'''
    print("Entrou no in")
    p[0] = p[1]

def p_out(p):
    '''out : OUTPUT VAR'''
    print("Entrou no out")
    p[0] = p[1]

def p_atrib(p):
    '''atrib : VAR AT expr'''
    print("Entrou no atrib")
    p[0] = p[1]

def p_expr(p):
    '''expr : term Y'''
    print("Entrou no expr")
    p[0] = p[1]

def p_Y(p):
    '''Y : empty
            | SUM expr
            | SUB expr'''
    print("Entrou no Y")
    p[0] = p[1]

def p_term(p):
    '''term : fact Z'''
    print("Entrou no term")
    p[0] = p[1]

def p_Z(p):
    '''Z : empty
            | MULT term
            | DIV term'''
    
    print("Entrou no Z")
    p[0] = p[1]

def p_fact(p):
    '''fact : NUM
            | VAR
            | OPEN expr CLOSE'''
    print("Entrou no fact")
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print("Syntax error in input!, rule: ", p)  
    print("Expected token: ")

# Build the parser
parser = yacc.yacc(method='SLR')

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    parser.parse(s)
