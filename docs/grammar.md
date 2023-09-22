prog   : line X
X      : EOF | prog
line   : stmt EOL
stmt   : in | out | atrib
in     : INPUT VAR
out    : OUTPUT VAR
atrib  : VAR AT expr
expr   : expr + term | expr - term | term
term   : term * fact | term / fact | fact
fact   : NUM | VAR | OE expr CE

EOL    : [\n\r]+
INPUT  : 'read'
OUTPUT : 'write'
VAR    : '$'[a-z]+
AT     : '='
OE     : '('
CE     : ')'
SUM    : '+'
SUB    : '-'
DIV    : '/'
MULT   : '*'