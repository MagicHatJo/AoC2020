#!/usr/bin/python3

def find_triple(entries):
	size = len(entries)
	for i in range(size - 2):
		l = i + 1
		r = size - 1
		while (l < r):
			if entries[i] + entries[l] + entries[r] == 2020:
				return entries[i] * entries[l] * entries[r]
			elif entries[i] + entries[l] + entries[r] < 2020:
				l += 1
			else:
				r -= 1

with open ("input") as f:
	entries = [int(i) for i in f.readlines()]
	entries.sort()
	print(find_triple(entries))