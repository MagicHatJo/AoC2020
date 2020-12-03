#!/usr/bin/python3
import re

with open("input") as f:
	data = f.readlines()

total = 0

for line in data:
	first, second, target, password = re.split('-| |: ', line)
	total += [password[int(first) - 1], password[int(second) - 1]].count(target) == 1

print(total)