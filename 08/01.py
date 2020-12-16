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

if __name__ == "__main__":
	with open("input") as f:
		data = [line.strip().split() for line in f]
		accumulator = 0
		execute(data)
		print(accumulator)