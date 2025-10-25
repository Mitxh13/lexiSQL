import ply.yacc as yacc
from lex import tokens, lexi as lexer

start = 'program'

def p_program_multiple(p):
    'program : statement program'

def p_program_single(p):
    'program : statement'

def p_program_empty(p):
    'program : empty'

def p_statements_multiple(p):
    'statements : statement statements'

def p_statements_single(p):
    'statements : statement'

def p_statements_empty(p):
    'statements : empty'

def p_statement_function(p):
    'statement : CREATE FUNCTION IDENTIFIER LPAREN RPAREN RETURNS data_type AS BEGIN statements END SEMICOLON'
    pass

def p_data_type(p):
    '''data_type : INT
                 | VARCHAR
                 | DATE
                 | FLOAT'''
    pass

def p_statement_if(p):
    'statement : IF condition THEN statements ELSE statements END IF SEMICOLON'
    pass

def p_statement_while(p):
    'statement : WHILE condition DO statements END WHILE SEMICOLON'
    pass

def p_statement_select(p):
    'statement : SELECT select_list FROM IDENTIFIER where_clause SEMICOLON'
    pass

def p_select_list(p):
    '''select_list : IDENTIFIER
                   | select_list COMMA IDENTIFIER'''
    pass

def p_where_clause(p):
    '''where_clause : WHERE condition
                    | empty'''
    pass

def p_condition(p):
    '''condition : IDENTIFIER EQUALS NUMBER
                 | IDENTIFIER GREATER NUMBER
                 | IDENTIFIER LESS NUMBER
                 | IDENTIFIER IN LPAREN number_list RPAREN'''
    pass

def p_number_list(p):
    '''number_list : NUMBER
                   | number_list COMMA NUMBER'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Parser ERROR: Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Parser ERROR: Syntax error at EOF")

parser = yacc.yacc()
