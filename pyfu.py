class PyFu():
	'''Brainfuck interpreter
	>>> PyFu(5).run('++++[>+++++<-]>[<+++++>-]<++++.+.')
	h
	i
	'''

	ops = '><+-[].,'
	
	switch = {
		'>': lambda s: s.dp_incr(),
		'<': lambda s: s.dp_decr(),
		'+': lambda s: s.mem_incr(),
		'-': lambda s: s.mem_decr(),
		'[': lambda s: s.l_bgn(),
		']': lambda s: s.l_end(),
		'.': lambda s: print(s.io_out()),
		',': lambda s: s.io_in(input('in?')),
	}
	
	def __init__(self,n):
		'''Set memory size
		>>> len(PyFu(5).mem)
		5
		'''
		self.reset(n)
	
	def __str__(self):
		'''Internal state can be printed out
		>>> str(PyFu(1))
		"PyFu mem: [0] dp: 0 ip: 0 code: ''"
		'''
		return 'PyFu mem: {} dp: {} ip: {} code: \'{}\''.format(self.mem, self.dp, self.ip, ''.join(self.code))
	
	def reset(self,n):
		'''Reset internal state, set memory size
		>>> p = PyFu(3)
		>>> p.mem
		[0, 0, 0]
		>>> p.code
		[]
		>>> p.dp
		0
		>>> p.ip
		0
		'''
		self.mem = [0]*n
		self.code = []
		self.dp = 0
		self.ip = 0
	
	def filter(code):
		'''General use Brainfuck code filter, only valid code remains
		>>> ''.join(PyFu.filter('abc+-[].,def<>'))
		'+-[].,<>'
		'''
		return [c for c in code if PyFu.ops.find(c) > -1]
	
	def run(self,code):
		'''Run code, code will be filtered and only valid opcodes will be used
		>>> p = PyFu(2)
		>>> p.run('inc > inc + done')
		>>> p.code
		['>', '+']
		>>> p.ip
		2
		>>> p.dp
		1
		>>> p.mem
		[0, 1]
		'''
		self.code = PyFu.filter(code)
		while self.ip < len(self.code):
			PyFu.switch[self.code[self.ip]](self)
			
	def ip_incr(self):
		''' Increase instruction pointer
		>>> p = PyFu(2)
		>>> p.ip_incr()
		>>> p.ip
		1
		'''
		self.ip = self.ip+1
	
	def ip_decr(self):
		''' Decrease instruction pointer
		>>> p = PyFu(2)
		>>> p.ip_decr()
		>>> p.ip
		-1
		'''
		self.ip = self.ip-1

	def dp_incr(self):
		''' > Increase data pointer
		>>> p = PyFu(2)
		>>> p.run('>')
		>>> p.dp
		1
		>>> p.ip
		1
		'''
		self.dp = self.dp+1
		self.ip_incr()
	
	def dp_decr(self):
		''' < Decrease data pointer
		>>> p = PyFu(2)
		>>> p.run('<')
		>>> p.dp
		-1
		>>> p.ip
		1
		'''
		self.dp = self.dp-1
		self.ip_incr()
	
	def mem_incr(self):
		''' + Increase memory value
		>>> p = PyFu(2)
		>>> p.run('+')
		>>> p.mem[p.dp]
		1
		>>> p.ip
		1
		'''
		self.mem[self.dp] = self.mem[self.dp]+1
		self.ip_incr()
	
	def mem_decr(self):
		''' - Decrease memory value
		>>> p = PyFu(2)
		>>> p.run('-')
		>>> p.mem[p.dp]
		-1
		>>> p.ip
		1
		'''
		self.mem[self.dp] = self.mem[self.dp]-1
		self.ip_incr()

	def l_bgn(self):
		''' Continues to next opcode or skips to loop end if current memory value is 0
		>>> p = PyFu(2)
		>>> p.mem[0] = 1
		>>> p.code = ['[','-',']']
		>>> p.l_bgn()
		>>> p.ip
		1
		>>> p.mem[0] = 0
		>>> p.code = ['[','-',']']
		>>> p.l_bgn()
		>>> p.ip
		2
		'''
		if self.mem[self.dp] == 0:
			while self.code[self.ip] != ']':
				self.ip_incr()
		else:
			self.ip_incr()
	
	def l_end(self):
		''' Continues to next opcode or backtracks to loop beginning if current memory value is not 0
		>>> p = PyFu(2)
		>>> p.mem[0] = 1
		>>> p.ip = 2
		>>> p.code = ['[','-',']']
		>>> p.l_end()
		>>> p.ip
		0
		>>> p = PyFu(2)
		>>> p.mem[0] = 0
		>>> p.ip = 2
		>>> p.code = ['[','-',']']
		>>> p.l_end()
		>>> p.ip
		3
		'''
		if self.mem[self.dp] == 0:
			self.ip_incr()
		else:
			while self.code[self.ip] != '[':
				self.ip_decr()

	def io_out(self):
		''' . Prints memory value as ASCII character
		>>> p = PyFu(1)
		>>> p.mem[p.dp] = 102
		>>> p.io_out()
		'f'
		>>> p.ip
		1
		'''
		self.ip_incr()
		return chr(self.mem[self.dp])
	
	def io_in(self,x):
		''' , Reads one ASCII character as memory value
		>>> p = PyFu(1)
		>>> p.io_in('')
		>>> p.mem[p.dp]
		0
		>>> p.io_in('hi')
		>>> p.mem[p.dp]
		104
		'''
		self.mem[self.dp] = 0 if len(x) == 0 else ord(x[0])
		self.ip_incr()

