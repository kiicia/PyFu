class PyFu():
	'''Brainfuck interpreter'''

	ops = '><+-[].,'
	
	switch = {
		'>': lambda s: s.dp_incr(),
		'<': lambda s: s.dp_decr(),
		'+': lambda s: s.mem_incr(),
		'-': lambda s: s.mem_decr(),
		'[': lambda s: s.l_bgn(),
		']': lambda s: s.l_end(),
		'.': lambda s: s.io_out(),
		',': lambda s: s.io_in(),
	}
	
	def __init__(self,n):
		'''Set memory size'''
		self.reset(n)
	
	def __str__(self):
		'''Internal state can be printed out'''
		return 'PyFu mem: {} dp: {} ip: {} code: \'{}\''.format(self.mem, self.dp, self.ip, ''.join(self.code))
	
	def reset(self,n):
		'''Reset internal state, set memory size'''
		self.mem = [0]*n
		self.code = []
		self.dp = 0
		self.ip = 0
	
	def filter(code):
		'''General use Brainfuck code filter, only valid code remains'''
		return [c for c in code if PyFu.ops.find(c) > -1]
	
	def run(self,code):
		'''Run code, code will be filtered and only valid opcodes will be used'''
		self.code = PyFu.filter(code)
		while self.ip < len(self.code):
			PyFu.switch[self.code[self.ip]](self)
			
	def ip_incr(self):
		self.ip = self.ip+1
	
	def ip_decr(self):
		self.ip = self.ip-1

	def dp_incr(self):
		self.dp = self.dp+1
		self.ip_incr()
	
	def dp_decr(self):
		self.dp = self.dp-1
		self.ip_incr()
	
	def mem_incr(self):
		self.mem[self.dp] = self.mem[self.dp]+1
		self.ip_incr()
	
	def mem_decr(self):
		self.mem[self.dp] = self.mem[self.dp]-1
		self.ip_incr()

	def l_bgn(self):
		if self.mem[self.dp] == 0:
			while self.code[self.ip] != ']':
				self.ip_incr()
		else:
			self.ip_incr()
	
	def l_end(self):
		if self.mem[self.dp] == 0:
			self.ip_incr()
		else:
			while self.code[self.ip] != '[':
				self.ip_decr()

	def io_out(self):
		print(chr(self.mem[self.dp]))
		self.ip_incr()
	
	def io_in(self):
		x = input('in?')
		self.mem[self.dp] = 0 if len(x) == 0 else ord(x[0])
		self.ip_incr()

