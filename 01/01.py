#!/usr/bin/python3

#read input

def find_pair():
	with open ("input") as f:
		entries = [int(i) for i in f.readlines()]

	table = {}

	for n in entries:
		if n in table:
			return n * (2020 - n)
		table[2020 - n] = True

print(find_pair())