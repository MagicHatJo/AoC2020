#!/usr/bin/python3

def get_differences(data):
	table = [0] * 4
	table[data[0]] += 1
	table[3] += 1
	for i in range(1, len(data)):
		table[data[i] - data[i - 1]] += 1
	return table[1] * table[3]

if __name__ == "__main__":
	with open("input") as f:
		data = [int(i) for i in f.readlines()]
		data.sort()
		print(get_differences(data))
