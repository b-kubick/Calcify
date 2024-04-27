from interpreter import Interpreter
from lexer import Lexer
from parsing import Parser
from tokenizer import Token

def main():
    while True:
        try:
            try:
                text = input('calcify> ')
            except NameError:
                text = input('calcify> ')
        except EOFError:
            break
        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
