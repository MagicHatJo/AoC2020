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

def get_contiguous(data, target):
	left = 0
	right = 0
	current = 0
	while left <= right and right < len(data):
		if current == target:
			return min(data[left:right]) + max(data[left:right])
		if current > target:
			current -= data[left]
			left += 1
		else:
			current += data[right]
			right += 1

if __name__ == "__main__":
	with open("input") as f:
		data = [int(i) for i in f.readlines()]

	invalid = get_invalid(data)
	print(get_contiguous(data, invalid))