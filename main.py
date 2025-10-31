from lex import lexi as lexer
import yacc

with open('test.sql','r') as f:
    data = f.read()

print("--- TOKENS USED ---")
lexer.input(data)
for tok in lexer:
    print(f"{tok.type:<12} -> {tok.value}")

print("\n--- PARSING --")
lexer.input(data)
lexer.lineno = 1 
yacc.parser.parse(data, lexer=lexer)

if not yacc.parse_errors:
    print("CODE IS PERFECT")