import ply.lex as lex

# List of token names.   This is always required
# EOL    : [\n\r]+
# INPUT  : 'read'
# OUTPUT : 'write'
# VAR    : '$'[a-z]+
# AT     : '='
# OE     : '('
# CE     : ')'
# SUM    : '+'
# SUB    : '-'
# DIV    : '/'
# MULT   : '*'
# NUM    : [0-9]+
tokens = (
    "EOF",
    "EOL",
    "INPUT",
    "OUTPUT",
    "VAR",
    "AT",
    "OPEN",
    "CLOSE",
    "SUM",
    "SUB",
    "DIV",
    "MULT",
    "NUM",
)


# Regular expression rules for simple tokens
t_EOL = r"[\n\r]+"
t_INPUT = r"read"
t_OUTPUT = r"write"
t_AT = r"="
t_OPEN = r"\("
t_CLOSE = r"\)"
t_SUM = r"\+"
t_SUB = r"\-"
t_DIV = r"\/"
t_MULT = r"\*"
t_VAR = r"\$[a-z]+"
def t_NUM(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t
def t_EOF(t):
    r'EOF'
    t.type = 'EOF'
    return t




# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"




# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

precedence = (
    ("left", "SUM", "SUB"),
    ("left", "MULT", "DIV"),
)

# Build the lexer
lexer = lex.lex()


import ply.yacc as yacc

# Parsing rules
# prog   : line X
# X      : EOF | prog
# line   : stmt EOL
# stmt   : in | out | atrib
# in     : INPUT VAR
# out    : OUTPUT VAR
# atrib  : VAR AT expr
# expr   : expr + term | expr - term | term
# term   : term * fact | term / fact | fact
# fact   : NUM | VAR | OE expr CE

start = "prog"

def p_prog(p):
    "prog : line X"
    print("prog")
    p[0] = p[1]

def p_X(p):
    "X : EOF"
    print("X")
    p[0] = p[1]

def p_X_prog(p):
    "X : prog"
    print("X")
    p[0] = p[1]

def p_line(p):
    "line : stmt EOL"
    print("Resultado: ", p[1])
    p[0] = p[1]

def p_stmt(p):
    "stmt : in"
    print("stmt")
    p[0] = p[1]

def p_stmt_out(p):
    "stmt : out"
    print("stmt")
    p[0] = p[1]

def p_stmt_atrib(p):
    "stmt : atrib"
    print("stmt")
    p[0] = p[1]

def p_in(p):
    "in : INPUT VAR"
    print("in")
    p[0] = p[1]

def p_out(p):
    "out : OUTPUT VAR"
    print("out")
    p[0] = p[1]

def p_atrib(p):
    "atrib : VAR AT expr"
    print("atrib")
    p[0] = p[3]

def p_expr(p):
    "expr : expr SUM term"
    print("expr")
    p[0] = p[1] + p[3]

def p_expr_sub(p):
    "expr : expr SUB term"
    print("expr")
    p[0] = p[1] - p[3]

def p_expr_term(p):
    "expr : term"
    print("expr")
    p[0] = p[1]

def p_term(p):
    "term : term MULT fact"
    print("term")
    p[0] = p[1] * p[3]

def p_term_div(p):
    "term : term DIV fact"
    print("term")
    p[0] = p[1] / p[3]

def p_term_fact(p):
    "term : fact"
    print("term")
    p[0] = p[1]

def p_fact_num(p):
    "fact : NUM"
    print("fact")
    p[0] = p[1]

def p_fact_var(p):
    "fact : VAR"
    print("fact")
    p[0] = p[1]

def p_fact_expr(p):
    "fact : OPEN expr CLOSE"
    print("fact")
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Erro de sintaxe na entrada: token '{p.value}' na linha {p.lineno}, coluna {p.lexpos}")
    else:
        print("Erro de sintaxe: Fim inesperado do arquivo (EOF)")



# Build the parser
parser = yacc.yacc(write_tables=False)

#Abrir o arquivo
f = open("entrada.txt", "r")
# Ler o arquivo
data = f.read()
# Fechar o arquivo
f.close()



result = parser.parse(lexer=lexer, input=data)
if result is not None:
    print("Parsing concluído com sucesso!")
else:
    print("Erro durante o parsing.")


