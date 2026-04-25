# simple-compiler

This activity derives from the code at [Simple Parser](https://github.com/Manchas2k4/tc3002b/tree/main/compilers/simple-parser) 

This is a recursive descent parser that builds and evaluates the AST for a custom grammar.

I completed the types and changed the methods to evaluate the AST.

This project tokenizes and parses a small language that supports:
- variable declarations (`VAR ...`)
- assignments (`:=`)
- `PRINT(...)`
- numeric expressions (`+ - * / MOD`)
- boolean/relational operators (`= <> < <= > >=`, `AND`, `OR`, unary `!`)
- boolean literals `#T` / `#F`
- comments using `%` (to end of line)

The grammar used is documented in [`grammar.txt`](./grammar.txt).


## Repository structure

- `main.py` — runs the parser against the sample programs under `test_cases/`
- `Lexer.py` — lexer/tokenizer (defines `Tag`, `Token`, and `Lexer.scan()`)
- `Parser.py` — recursive-descent parser that builds an AST and evaluates it
- `SymbolTable.py` — symbol table/environment used during evaluation
- `Nodes/` — AST node implementations
    - These include the abstract class definitions for the tokens. These were separated for easier maintenance or adding new methods
- `test_cases/` — sample “good” programs and “bad” programs
    - I added some more cases to test the grammar


## Requirements

- Python 3.7 or above due to dataclass annotations

## How to run

From the repository root:

```bash
python3 main.py
```

What it does:
- Parses and evaluates every file in `test_cases/good/*.txt` (these should succeed)
- Parses and evaluates every file in `test_cases/bad/*.txt` (these should raise an error)

## Notes / limitations

- The parser is a hand-written recursive descent parser using FIRST sets.
- Input programs are read from files (see `test_cases/`).
- Error messages include line information from the lexer.