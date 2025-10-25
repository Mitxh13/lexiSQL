import ply.lex as lex

tokens = [
    'CREATE', 'TABLE', 'INSERT', 'INTO', 'VALUES',
    'PRIMARY', 'KEY',
    'INT', 'VARCHAR', 'DECIMAL', 'DATE',
    'IDENTIFIER', 'NUMBER', 'STRING',
    'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON'
]

reserved = {
    'CREATE': 'CREATE',
    'TABLE': 'TABLE',
    'INSERT': 'INSERT',
    'INTO': 'INTO',
    'VALUES': 'VALUES',
    'PRIMARY': 'PRIMARY',
    'KEY': 'KEY',
    'INT': 'INT',
    'VARCHAR': 'VARCHAR',
    'DECIMAL': 'DECIMAL',
    'DATE': 'DATE'
}

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'IDENTIFIER') 
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]  
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Lexer ERROR: Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexi = lex.lex()
