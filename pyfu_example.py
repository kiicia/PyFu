from pyfu import PyFu

print_ascii = '''

++++++
[
>++++++++
<-
]
>>
++++++++
[
<<++++++++++
>>-
]
<<
[
>>>+<<<
>.+
<-
]
'''

pf = PyFu(4)
print(pf)
#pf.run('>,<+++[>+<-]>.>--')
pf.run(print_ascii)
print(pf)

