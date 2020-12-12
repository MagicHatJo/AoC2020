#!/usr/bin/python3

def create_layout(data):
	layout = {}
	for i, row in enumerate(data):
		for j, v in enumerate(row):
			layout[complex(i, j)] = v
	return layout

def cycle_seats(layout):
	new = {}
	for key in layout.keys():
		occupied = sum(layout.get(key + offset) == '#' for offset in [-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j])
		if layout[key] == 'L' and occupied == 0:
			new[key] = '#'
		elif layout[key] == '#' and occupied >= 4:
			new[key] = 'L'
		else:
			new[key] = layout[key]
	return new

def stabilize(layout):
	new = cycle_seats(layout)
	while layout != new:
		layout = new
		new = cycle_seats(layout)
	return layout

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split()
		layout = create_layout(data)
		result = stabilize(layout)
		print(sum(c == '#' for c in result.values()))