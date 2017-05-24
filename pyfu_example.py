from pyfu import PyFu

print_ascii = '''
Example Brainfuck code; will print a sequence of ASCII characters; do not use valid opcodes in comments

1) preinitializing memory location 1 to 6*8 (ASCII start value)
++++++
[
>++++++++
<-
]

2) skipping over to location 2
>>

3) preinitializing location 0 to 8*10 (main loop counter)
++++++++
[
<<++++++++++
>>-
]

4) skipping to location 0
<<

5) main loop; based on value in location 0
[
>>>+<<< (increment counter in location 3)
>.+ (print out and increment value in location 1)
<- (decrement loop counter in location 0)
]
'''

pf = PyFu(4)
print(pf)
pf.run(print_ascii)
print(pf)

