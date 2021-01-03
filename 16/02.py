#!/usr/bin/python3

import re

def parse_rules(data):
	rules = {}
	data =  [re.split(r': |-| or ', line) for line in data.split('\n')]
	for line in data:
		rules[line[0]] = set(range(int(line[1]), int(line[2]) + 1))
		rules[line[0]].update(range(int(line[3]), int(line[4]) + 1))
	return rules

def parse_ticket(data):
	return [[int(n) for n in line.split(',')] for line in re.split(r'\n', data)[1:]]

def populate_lookup(data):
	lookup = set()
	for line in data.values():
		lookup |= line
	return lookup

def toss_invalid(rules, data):
	lookup = populate_lookup(rules)
	return [line for line in data if set(line).issubset(lookup)]

def check_col(data, confirmed, unknown_columns, unknown_rules, col):
	index_list = []
	rule_cache = None
	for rule in unknown_rules:
		if set([line[col] for line in data]).issubset(set(rules[rule])):
			index_list.append(col)
			rule_cache = rule
	if len(index_list) == 1:
		confirmed[rule_cache] = index_list[0]
		unknown_columns.remove(index_list[0])
		unknown_rules.remove(rule_cache)
		return True
	return False

def match_rules(rules, data):
	confirmed = {}
	unknown_columns = set(range(len(data[0])))
	unknown_rules   = set(rules.keys())

	for i in range(len(data[0])):
		for col in unknown_columns:
			if check_col(data, confirmed, unknown_columns, unknown_rules, col):
				break

	return confirmed

if __name__ == "__main__":
	with open("input", 'r') as f:
		data   = f.read().split("\n\n")
		rules  = parse_rules(data[0])
		mine   = parse_ticket(data[1])[0]
		nearby = toss_invalid(rules, parse_ticket(data[2]))

		rule_index = match_rules(rules, nearby)

		print(
			mine[rule_index["departure track"]] *
			mine[rule_index["departure station"]] *
			mine[rule_index["departure platform"]] *
			mine[rule_index["departure location"]] *
			mine[rule_index["departure time"]] *
			mine[rule_index["departure date"]]
		)