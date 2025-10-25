# SQL Lexer using PLY

## Overview
The lexer identifies and categorizes SQL tokens like keywords, datatypes, operators, symbols, and identifiers.
It demonstrates how a lexical analyzer breaks down SQL code into meaningful tokens — the first step in building a compiler or interpreter.

---

## Features

1. **Function Declaration / Definition** – `CREATE FUNCTION ... RETURNS ...`
2. **Simple Data Type Declaration** – `INT`, `VARCHAR`, `DATE`, `FLOAT`
3. **Selection Statements** – `IF`, `THEN`, `ELSE`, `CASE`, `WHEN`
4. **Looping Construct** – `WHILE`, `DO`, `END WHILE`
5. **Array / List Representation** – using `IN ( ... )`

---

## 📦 Requirements

* Python
* PLY library
Install PLY using:

```bash
pip install ply
```

---

## Project Structure
```
SQL-Lexer-using-PLY/
│
├── lex.py        # Main lexer implementation
├── test.sql      # Sample SQL input file
└── README.md     # Project documentation
```

---

## To Use

1. Clone this repository:
   ```bash
   git clone https://github.com/Mitxh13/lexiSQL.git
   cd lexiSQL
   ```
2. Run the lexer:
   ```bash
   python lex.py
   ```
3. The lexer will display tokenized output for the given SQL input.

---

## Team
1) **Kurumeti Mitesh**
2) **Tahir**
