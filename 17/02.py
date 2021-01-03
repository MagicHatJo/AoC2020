#!/usr/bin/python3

import numpy as np
from scipy.signal import convolve

def cubify(data):
	return np.array([list(map(lambda x: 1 if x == '#' else 0, line)) for line in data], dtype=np.uint8)

def advance(cube, dimension, cycles):
	grid = cube.reshape([1] * (dimension - len(cube.shape)) + list(cube.shape))
	kernel = np.ones([3] * dimension, dtype=np.uint8)
	for i in range(cycles):
		c = convolve(grid, kernel)
		grid = np.pad(grid, ((1, 1),), mode='constant') & (c == 4) | (c == 3)
	return np.sum(grid)

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().splitlines()
		cube = cubify(data)
		print(advance(cube, 4, 6))