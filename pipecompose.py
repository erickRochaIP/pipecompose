class Chain:
	def __init__(self, value):
		self.value = value

	def __or__(self, function):
		return Chain(self > function)

	def __gt__(self, function):
		return function(self.value)

get = lambda x: x
attr = lambda *args: lambda x: (rec_attr := lambda x, *args:  x if not args else rec_attr(x[args[0]], *(args[1:])))(x, *args)
call = lambda function: lambda *args: lambda x: function(x, *args)
