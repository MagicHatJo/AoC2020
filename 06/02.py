#!/usr/bin/python3

with open("input") as f:
	data = f.read().split("\n\n")

total = 0
for line in data:
	line = line.split()
	s = set(line[0])
	for a in line:
		s = s.intersection(a)
	total += len(s)
print(total)