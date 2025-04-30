class curry:
	def __init__(self, fun, *args):
		self.fun = fun
		if args[len(args) - 1] == "Lazy":
			self.eager = False
			self.args = args[0:(len(args) - 1)]
		else:
			self.eager = True
			self.args = (args[0],)

	def __call__(self, *args):
		if len(args) > 0:
			if self.eager:
				q = self.args[0]
				for i in args:
					q = self.fun(q, i)
				return curry(self.fun, q)
			else:
				return curry(self.fun, *(self.args + args + ("Lazy",)))
		else:
			if self.eager:
				return self.fun(self.args[0], 0)
			else:
				if len(self.args) > 1:
					q = 0
					for i in self.args:
						q = self.fun(q, i)
					self.args = (q,)
				return self.fun(self.args[0], 0)

print
add2 = lambda x, y : x + y
adder = curry(add2, 5)
adder = adder(3)
print adder()
print adder(2)()
print adder(1)()
adder = adder(3)
print adder()
print

adder0 = curry(add2, 0)
adder18 = adder0(3)(4,5)(6)
print adder18()
print adder18(2)()
print

lazyAdder0 = curry(add2, 0, "Lazy")
lazyAdder18 = lazyAdder0(3)(4,5)(6)
print lazyAdder18()
print lazyAdder18(2)()
print

def sleepingAdd(x, y):
	import time
	for i in xrange(0, y):
		print ".",
		time.sleep(0.1);
	return x + y;

sadder0 = curry(sleepingAdd, 0)
print "Hey",
sadder10 = sadder0(3)(4,2)(1)
print "Yo"
print sadder10()
print "Hey",
sadder10()
print "Yo"
print

lazySadder0 = curry(sleepingAdd, 0, "Lazy")
print "Hey",
lazySadder10 = lazySadder0(3)(4,2)(1)
print "Yo"
print lazySadder10()
print "Hey",
lazySadder10()
print "Yo"
print
