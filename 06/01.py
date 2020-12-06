#!/usr/bin/python3

with open("input") as f:
	data = f.read().split("\n\n")

total = 0
for line in data:
	s = set(line)
	if '\n' in s:
		s.remove("\n")
	total += len(s)
print(total)