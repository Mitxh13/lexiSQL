import ply.yacc as yacc
from lex import tokens, lexi

parse_errors = False

start = 'program'

def p_program_multiple(p):
    'program : statement program'
    pass

def p_program_single(p):
    'program : statement'
    pass

def p_statement_create_table(p):
    'statement : CREATE TABLE IDENTIFIER LPAREN column_def_list RPAREN SEMICOLON'
    print(f"CREATE TABLE parsed: {p[3]}")

def p_statement_insert(p):
    'statement : INSERT INTO IDENTIFIER LPAREN column_list RPAREN VALUES value_list SEMICOLON'
    print(f"INSERT INTO parsed: {p[3]}")

def p_column_def_list_multiple(p):
    'column_def_list : column_def_list COMMA column_def'
    pass

def p_column_def_list_single(p):
    'column_def_list : column_def'
    pass

def p_column_def(p):
    '''column_def : IDENTIFIER data_type
                  | IDENTIFIER data_type PRIMARY KEY'''
    pass

def p_data_type(p):
    '''data_type : INT
                 | VARCHAR LPAREN NUMBER RPAREN
                 | DECIMAL LPAREN NUMBER COMMA NUMBER RPAREN
                 | DATE'''
    pass

def p_column_list_multiple(p):
    'column_list : column_list COMMA IDENTIFIER'
    pass

def p_column_list_single(p):
    'column_list : IDENTIFIER'
    pass

def p_value_list_multiple(p):
    'value_list : value_list COMMA LPAREN row_values RPAREN'
    pass

def p_value_list_single(p):
    'value_list : LPAREN row_values RPAREN'
    pass

def p_row_values_multiple(p):
    'row_values : row_values COMMA value'
    pass

def p_row_values_single(p):
    'row_values : value'
    pass

def p_value(p):
    '''value : NUMBER
             | STRING
             | DATE'''
    pass

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    global parse_errors
    parse_errors = True
    if p:
        print(f"Parser ERROR: Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Parser ERROR: Syntax error at EOF (maybe missing semicolon)")


parser = yacc.yacc()
