#!/usr/bin/python3

import re

def mask_value(num, mask):
	m0 = int(mask.replace("X", "0"), 2)
	m1 = int(mask.replace("X", "1"), 2)
	return (num | m0) & m1

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = [re.compile("^(\w*)(?:\[(\d+)\]|)\s=\s([0-9X]+)$").findall(l) for l in f.readlines()]

		memory = {}
		mask = ''
		for [(op, address, value)] in data:
			if op == "mask":
				mask = value
			else:
				memory[address] = mask_value(int(value), mask)
		print(sum(memory.values()))
