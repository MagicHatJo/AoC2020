#!/usr/bin/python3

def memory_game(start, target):
	spoken = {k: v for v, k in enumerate(start)}
	current = start[-1]
	for i in range(len(start) - 1, target - 1):
		spoken[current], current = i, i - spoken[current] if current in spoken else 0
	return current

if __name__ == "__main__":
	data = [19,20,14,0,9,1]
	print(memory_game(data, 2020))