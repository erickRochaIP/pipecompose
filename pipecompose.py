class Chain:
	def __init__(self, value):
		self.value = value

	def __or__(self, function):
		return Chain(self > function)

	def __gt__(self, function):
		return function(self.value)

	def __invert__(self):
		return self.value
	
	def pipe(self, function):
		return self | function
	
	def get(self):
		return ~self

get = lambda x: x
_rec_op = lambda op: lambda *args: lambda x: (rec_op := lambda x, *a: x if not a else rec_op(op(x, a[0]), *(a[1:])))(x, *args)

attr = _rec_op(lambda x, a: x[a])
compose = _rec_op(lambda x, f: f(x))

_apply = lambda op: lambda f: lambda *args: lambda x: op(x, f, *args)

call = _apply(lambda x, f, *args: f(x, *args))
map = _apply(lambda x, f, *args: [f(it, *args) for it in x])
