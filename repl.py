from hawkparser import Parser
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def repl():
    print('Hawklang REPL')
    print('Type CLS to clear, and EXIT to exit.')
    while True:
        code = input('>>>')
        if code == 'CLS': clear()
        elif code == 'EXIT': break
        else: Parser(code).parse()