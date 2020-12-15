#!/usr/bin/python3

import re

def generate_address(address, mask):
	address |= int(mask.replace("X", "0"), 2)
	address = list(bin(address)[2:].zfill(36))
	x_pos = [i for i, v in enumerate(mask) if v == 'X']

	for combination in range(1 << len(x_pos)):
		for i, bit in enumerate(bin(combination)[2:].zfill(len(x_pos))):
			address[x_pos[i]] = bit
		yield ''.join(address)

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = [re.compile("^(\w*)(?:\[(\d+)\]|)\s=\s([0-9X]+)$").findall(l) for l in f.readlines()]

		memory = {}
		mask = ''
		for [(op, address, value)] in data:
			if op == "mask":
				mask = value
			else:
				for location in generate_address(int(address), mask):
					memory[location] = int(value)
		print(sum(memory.values()))