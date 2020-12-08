#!/usr/bin/python3

def do_acc(i, n):
	global accumulator
	accumulator += n
	return i + 1

def do_jmp(i, n):
	return i + n

def do_nop(i, n):
	return i + 1

def execute(data):
	visitted = set()

	dispatch = {
		"acc": do_acc,
		"jmp": do_jmp,
		"nop": do_nop
	}

	i = 0
	while i not in visitted and i < len(data):
		visitted.add(i)
		i = dispatch[data[i][0]](i, int(data[i][1]))
	return i

def mutate(data):
	for i in range(len(data)):
		if data[i][0] == 'jmp':
			data[i][0] = "nop"
			yield data
			data[i][0] = "jmp"
		elif data[i][0] == "nop":
			data[i][0] = "jmp"
			yield data
			data[i][0] = "nop"

if __name__ == "__main__":
	with open("input") as f:
		data = [line.strip().split() for line in f]

	for d in mutate(data):
		accumulator = 0
		if execute(d) == len(d):
			print(accumulator)
			break