#!/usr/bin/python3

def binary_split(string, lc, hc, low, high):

	if len(string) == 1:
		return low if string == lc else high

	mid = (low + high) // 2
	if string[0] == lc:
		return binary_split(string[1:], lc, hc, low, mid - 1)
	else:
		return binary_split(string[1:], lc, hc, mid + 1, high)

with open("input") as f:
	data = f.read().split("\n")

	m = 0
	for line in data:
		row = binary_split(line[:7], 'F', 'B', 0, 127)
		col = binary_split(line[7:], 'L', 'R', 0, 7)
		m = max(m, row * 8 + col)

	print(m)
