
def get_coordinates(data):
	axial = {
		"w" : -1+0j,
		"nw":  0-1j,
		"ne":  1-1j,
		"e" :  1+0j,
		"se":  0+1j,
		"sw": -1+1j
	}

	coordinates = {}
	for line in data:
		current = 0
		while line:
			nxt = 1 + (line[0] in "ns")
			current += axial[line[:nxt]]
			line = line[nxt:]
		coordinates[current] = ~coordinates.get(current, False)
	return coordinates

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n")
		
		tiles = get_coordinates(data)
		print(sum(1 for i in tiles if tiles[i]))