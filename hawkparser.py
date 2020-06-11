class Parser:
    def __init__(self, text):
        self.pool = ['0'] * 8
        self.cache = ['0'] * 8
        self.pointer = 0
        self.onerror = False
        self.code = text.split('\n')
        self.buffer = ''

    def parse(self):
        counter = 0
        for line in self.code:
            res = []
            res[:] = line
            #print(res)
            for pos, char in enumerate(res):
                #print(char, pos)
                if char == '>': # Clears the pool
                    self.pool = ['0'] * 8
                    self.pointer = 0

                elif char == '\\': # Moves the pointer left one bit
                    if self.pointer == 0:
                        self.error(1, counter, pos)
                        break
                    self.pointer -=1

                elif char == '/':  # Moves the pointer right one bit
                    if self.pointer == 7:
                        self.error(1, counter, pos)
                        break
                    self.pointer += 1

                elif char == '^': # Inverses bit under pointer
                    if self.pool[self.pointer] == '0': self.pool[self.pointer] = '1'
                    else: self.pool[self.pointer] = '0'

                elif char == '!': # Inverses all bits in pool
                    for _, item in enumerate(self.pool):
                        if item == '0': self.pool[_] = '1'
                        else: self.pool[_] = '0'
                    #print(self.pool)

                elif char == ':': # Reads the pool as a 8 bit integer and prints the ascii value of it
                    if chr(int(''.join(self.pool))) == '\n':
                        self.buffer += '\n'
                    else:
                        self.buffer += chr(int(''.join(self.pool), 2))

                elif char == '.': # Saves pool to cache
                    if self.pool == ['0'] * 8:
                        self.error(3, counter, pos)
                        break
                    self.cache = self.pool

                elif char == ',': # Saves cache to pool
                    if self.cache == ['0'] * 8:
                        self.error(2, counter, pos)
                        break
                    self.pool = self.cache

                elif char == '+': # Clears cache
                    if self.cache == ['0'] * 8:
                        self.error(4, counter, pos)
                        break

                    self.cache = ['0'] * 8




            if self.onerror:
                break

            #print()

            counter += 1

        if not self.onerror: # Print
            print(self.buffer)
            print()

    def error(self, code, line, char):
        pos = f'{line+1};{char+1}'
        if code == 1: # User attempted to move pointer out of pool range (<0, >7)
            print(f'''
ERROR (code 1) in {pos} of code
Pointer moved outside of pool. Remember: the Pool is only 8 bits large!
''')

        elif code == 2: # User attempted to dump an empty cache
            print(f'''
ERROR (code 2) in {pos} of code
Cannot dump an empty cache!
''')

        elif code == 3: # User attempted to save an empty pool to cache
            print(f'''
ERROR (code 3) in {pos} of code
Cannot save an empty pool!
''')

        elif code == 4: # User attempted to clear an empty cache
            print(f'''
ERROR (code 4) in {pos} of code
Cannot clear an empty cache!
''')
        self.onerror = True