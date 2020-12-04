#!/usr/bin/python3

with open("input") as f:
	data = f.read().split("\n\n")

count = 0
for line in data:
	d = {}
	info = line.split()
	for pair in info:
		d[pair[0:3]] = pair[4:]
	
	count += (len(d) == 8 or (len(d) == 7 and "cid" not in d))

print(count)