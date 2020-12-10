#!/usr/bin/python3

def count_connections(start, data, memo={}):
	if start == data[-1]:
		return 1
	count = 0
	for i in range(1, 4):
		if start + i in data:
			if start + i not in memo:
				memo[start + i] = count_connections(start + i, data, memo)
			count += memo[start + i]
	return count

if __name__ == "__main__":
	with open("input") as f:
		data = [int(i) for i in f.readlines()]
		data.sort()
		print(count_connections(0, data))