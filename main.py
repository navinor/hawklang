import sys
from hawkparser import Parser
from repl import repl

try:
    code = open(sys.argv[1]).read()
    Parser(code).parse()
except:
    print('Starting Hawklang REPL...')
    repl()
