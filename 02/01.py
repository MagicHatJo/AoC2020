#!/usr/bin/python3
import re

with open("input") as f:
	data = f.readlines()

total = 0

for line in data:
	low, high, target, password = re.split('-| |: ', line)
	
	if int(low) <= password.count(target) <= int(high):
		total += 1

print(total)