#!/usr/bin/python3

import re

def parse_rules(data):
	return [re.split(r': |-| or ', line) for line in data.split('\n')]

def parse_ticket(data):
	return re.split(r',|\n', data)[1:]

def populate_lookup(data):
	lookup = set()
	for line in data:
		for i in range(int(line[1]), int(line[2]) + 1):
			lookup.add(i)
		for i in range(int(line[3]), int(line[4]) + 1):
			lookup.add(i)
	return lookup

def count_invalid(data, lookup):
	total = 0
	for num in data:
		if int(num) not in lookup:
			total += int(num)
	return total

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n\n")
		rules = parse_rules(data[0])
		mine = parse_ticket(data[1])
		nearby = parse_ticket(data[2])

		lookup = populate_lookup(rules)
		print(count_invalid(nearby, lookup))