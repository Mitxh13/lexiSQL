import ply.lex as lex

tokens = [
    'CREATE', 'FUNCTION', 'RETURNS', 'AS', 'BEGIN', 'END', 'WHILE', 'DO',
    'IF', 'THEN', 'ELSE', 'IN', 'SELECT', 'FROM', 'WHERE',
    'INT', 'VARCHAR', 'DATE', 'FLOAT',
    'IDENTIFIER', 'NUMBER', 'STRING',
    'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON', 'EQUALS','GREATER','LESS'
]

t_CREATE = r'CREATE'
t_FUNCTION = r'FUNCTION'
t_RETURNS = r'RETURNS'
t_AS = r'AS'
t_BEGIN = r'BEGIN'
t_END = r'END'
t_WHILE = r'WHILE'
t_DO = r'DO'
t_IF = r'IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_IN = r'IN'
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_INT = r'INT'
t_VARCHAR = r'VARCHAR'
t_DATE = r'DATE'
t_FLOAT = r'FLOAT'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQUALS = r'='
t_GREATER = r'>'
t_LESS = r'<'

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Lexer ERROR: Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexi = lex.lex()
