
AXIAL = {
	"w" : -1+0j,
	"nw":  0-1j,
	"ne":  1-1j,
	"e" :  1+0j,
	"se":  0+1j,
	"sw": -1+1j
}

def get_coordinates(data):
	coordinates = {}
	for line in data:
		current = 0
		while line:
			nxt = 1 + (line[0] in "ns")
			current += AXIAL[line[:nxt]]
			line = line[nxt:]
		coordinates[current] = ~coordinates.get(current, False)
	return set([key for key in coordinates if coordinates[key]])

def check_active(coordinate, old, new, adjacent):
	neighbors = {coordinate + direction for direction in AXIAL.values()}
	if len(neighbors & old) in {1, 2}:
		new.add(coordinate)
	adjacent.update(neighbors)

def check_adjacent(coordinate, old, new):
	neighbors = {coordinate + direction for direction in AXIAL.values()}
	n = len(neighbors & old)
	if n == 2 or (coordinate in old and n == 1):
		new.add(coordinate)

def next_day(tiles):
	new = set()
	adjacent = set()
	for coordinate in tiles:
		check_active(coordinate, tiles, new, adjacent)
	for coordinate in adjacent:
		check_adjacent(coordinate, tiles, new)
	return new

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n")

		tiles = get_coordinates(data)
		for _ in range(100):
			tiles = next_day(tiles)
		print(len(tiles))
			
