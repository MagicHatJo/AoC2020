#!/usr/bin/python3

def shunting_yard(s):
	stack = []
	ops = ['+', '*']
	for c in list(s.replace(' ', '')):
		if c.isdigit():
			yield c
		elif c in ops:
			while stack and stack[-1] in ops:
				yield stack.pop()
			stack.append(c)
		elif c == '(':
			stack.append(c)
		elif c == ')':
			while stack and stack[-1] != '(':
				yield stack.pop()
			stack.pop()
	while stack:
		yield stack.pop()

def calculate(s):
	stack = []
	dispatch = {
		'+': lambda: stack.append(stack.pop() + stack.pop()),
		'*': lambda: stack.append(stack.pop() * stack.pop())
	}
	for token in shunting_yard(s):
		try:	dispatch[token]()
		except:	stack.append(int(token))
	return stack.pop()

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		print(sum([calculate(line) for line in data]))
