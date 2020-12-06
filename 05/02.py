#!/usr/bin/python3

def get_seats(str):
	return int(str.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)

with open("input") as f:
	data = f.readlines()

	seats = [get_seats(line) for line in data]
	missing = set(range(max(seats))).difference(seats)
	for num in missing:
		if num + 1 not in missing and num - 1 not in missing:
			print(num)