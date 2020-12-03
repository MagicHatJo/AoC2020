#!/usr/bin/python3

with open("input") as f:
	projection = f.read().splitlines()

def get_trees(projection, dr, dd):
	count = 0
	x = dr
	y = dd
	while (y < len(projection)):
		count += projection[y][x % len(projection[0])] == '#'
		x += dr
		y += dd
	return count

print(
	get_trees(projection, 1, 1) *
	get_trees(projection, 3, 1) *
	get_trees(projection, 5, 1) *
	get_trees(projection, 7, 1) *
	get_trees(projection, 1, 2)
)