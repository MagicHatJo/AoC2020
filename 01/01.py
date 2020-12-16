#!/usr/bin/python3

def find_pair(entries):
	table = {}
	for n in entries:
		if n in table:
			return n * (2020 - n)
		table[2020 - n] = True

with open ("input") as f:
	entries = [int(i) for i in f.readlines()]
	print(find_pair(entries))