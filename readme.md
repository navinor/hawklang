# Hawklang
## An esoteric language ~~copied~~ heavily inspired by [Excon](https://esolangs.org/wiki/EXCON)

### How it works
Hawklang starts with a pool of 8 bits, and a cache of 8 bits as well. Both automatically start as `00000000`.
Hawklang also has a pointer, which automatically starts at position 0 
```
00000000
^
```



Hawklang has 8 instructions. Listed below are the instructions, and their actions.
```
>               |     Clears the Pool (to 00000000), and moves the pointer back to position 0
/               |     Moves the pointer right one bit.
\               |     Moves the pointer left one bit.
^               |     Inverses the bit that is under the pointer (1 -> 0, 0 -> 1)
!               |     Inverses all the bits in the pool
:               |     Reads the pool as a 8-bit integer and prints out the ascii value of it
.               |     Saves pool to cache
,               |     Dumps cache to pool
+               |     Clears cache
```
Any other characters that are not >/\^!:., are considered comments.

### Important Note
If you are dealing with, for example, the letter H, which in binary is only 7 bits long (1001000), 
make sure you leave an extra zero before the first 1 (01001000), so that the parser doesn't read it as 10010000!
(10010000 as an ascii character is `\x90`, which is definitely not H!)

## Examples

example1.hawk | Prints the letter 'A'
```
'A' in binary is 01000001 so we need to flip the bits at position 1 and position 7
>          First clear the pool (optional)
/^         Move the pointer left one bit and flip that bit
//////^    Move the pointer left six more bits and flip the last bit
:>         Print out the pool (A) and clear the pool
```



example2.hawk | Prints Hello world!
```
>/^///^:      Prints 'H' (01001000) (Note the beginning zero)
>/^/^///^//^: Prints 'e' (01100101)
>/^/^//^/^:.  Prints 'l' and saves it to cache (01101100)
>,:+          Prints 'l' from cache and clears cache
>!^///^:.     Prints 'o' and saves it to cache (01101111)
>//^:         Prints ' ' (00100000)
>!^////^:     Prints 'w' (01110111)
>,:+          Prints 'o' from cache and clears cache
>/^/^/^///^:  Prints 'r' (01110010)
>/^/^//^/^:   Prints 'l' (01101100)
>/^/^///^:    Prints 'd' (01100100)
>//^/////^:   BANG (00100001)
>////^//^:    Prints a newline (00001010)
```
The following can also be written like this:
```
>/^///^:>/^/^///^//^:>/^/^//^/^:.>,:+>!^///^:.>//^:>!^////^:>,:+>/^/^/^///^:>/^/^//^/^:>/^/^///^:>//^/////^:>////^//^:
```


## Usage Instructions
If you want to use the .exe file, simply run `hawklang.exe` to access the Hawklang REPL, or open command prompt,
navigate to the directory hawklang.exe is in, and run  `hawklang [insert hawk file here]` to run a hawklang file.

### Screenshots
![image](https://storage.googleapis.com/replit/images/1591915172564_691f4b4690d0176951cba04f829d37ac.png)


![image](https://storage.googleapis.com/replit/images/1591915234890_fc3931ac5ea8f5742d738f7f50ebd49c.png)

> ## Have fun!
> cheers, Warhawk947
