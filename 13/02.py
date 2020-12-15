#!/usr/bin/python3

def parse_id(id_list):
	new = []
	for i, v in enumerate(id_list):
		if v != 'x':
			new.append((-i % int(v), int(v)))
	return new

def chinese_remainder(pairs):
	remainder = 0
	coefficient = 1

	for equation in pairs:
		co = coefficient
		for i in range(1, equation[1]):
			if (co * i) % equation[1] == 1:
				remainder = (equation[0] - remainder) * i % equation[1] * coefficient + remainder
				coefficient = coefficient * equation[1]
				break
	return remainder

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		print(chinese_remainder(parse_id(data[1].split(','))))