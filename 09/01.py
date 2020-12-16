#!/usr/bin/python3

def check_two_sum(data, target):
	table = {}

	for n in data:
		if n in table:
			return True
		table[target - n] = True
	
	return False

def get_invalid(data):
	left = 0
	right = 25
	while right < len(data):
		if not check_two_sum(data[left:right], data[right]):
			return data[right]
		left  += 1
		right += 1

if __name__ == "__main__":
	with open("input") as f:
		data = [int(i) for i in f.readlines()]
		print(get_invalid(data))