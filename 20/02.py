
class Tile:
	def __init__(self, data):
		data = data.split()
		self.id = int(data[1][:-1])
		self.data = [list(line) for line in data[2:]]		
		self.size = len(self.data)
		self.borders = self.get_borders()
		self.calibrated = False

	def rotate(self):
		for x in range(self.size // 2):
			for y in range(x, self.size - x - 1):
				self.data[x][y], self.data[y][self.size-1-x], self.data[self.size-1-x][self.size-1-y], self.data[self.size-1-y][x] = \
				self.data[y][self.size-1-x], self.data[self.size-1-x][self.size-1-y], self.data[self.size-1-y][x], self.data[x][y]

	def flip(self):
		self.data = [list(reversed(row)) for row in self.data]
	
	def vflip(self):
		self.data = list(reversed(self.data))

	def get_borders(self):
		b = [self.data[0][:]]
		for transform in [self.rotate, self.rotate, self.rotate, self.flip, self.rotate, self.rotate, self.rotate]:
			transform()
			b.append(self.data[0][:])
		return b
	
	def get_side(self, side):
		return {
			"left" : [row[0] for row in self.data],
			"right": [row[-1] for row in self.data],
			"top"  : self.data[0],
			"bot"  : self.data[-1]
		}[side]
	
	def trim(self):
		self.data = [row[1:-1] for row in self.data[1:-1]]

	def __repr__(self):
		out = ""
		for row in self.data:
			for c in row:
				out += c
			out += "\n"
		return out

def generate_links(pool):
	links = {tile.id: [] for tile in pool}
	for i, first in enumerate(pool):
		for k, second in enumerate(pool):
			if i != k and any(j in first.borders for j in second.borders):
				links[first.id].append(second.id)
	return links

def calculate_borders(image_id, available, links, size):
	def rotate(image, size):
		for x in range(size // 2):
			for y in range(x, size - x - 1):
				image[x][y], image[y][size-1-x], image[size-1-x][size-1-y], image[size-1-y][x] = \
				image[y][size-1-x], image[size-1-x][size-1-y], image[size-1-y][x], image[x][y]

	for _ in range(4):
		for x in range(1, size):
			if image_id[0][x] == 0:
				for tile_id in links[image_id[0][x - 1]]:
					if len(links[tile_id]) < 4 and tile_id in available:
						image_id[0][x] = tile_id
						available.remove(tile_id)
						break
		rotate(image_id, size)

def calculate_jigsaw(image_id, available, links, size):
	for y in range(1, size - 1):
		for x in range(1, size - 1):
			num = (set(links[image_id[y][x - 1]]) & set(links[image_id[y - 1][x]]) & available).pop()
			image_id[y][x] = num
			available.remove(num)

def build_image_id(links, size):
	image_id = [[0 for i in range(size)] for k in range(size)] 
	available = set(links.keys())

	for tile_id in links:
		if len(links[tile_id]) == 2:
			image_id[0][0] = tile_id
			available.remove(tile_id)
			break

	calculate_borders(image_id, available, links, size)
	calculate_jigsaw(image_id, available, links, size)
	return image_id

def calibrate_tile(tiles, idx, target, direction):
	for _ in range(2):
		for __ in range(4):
			if tiles[idx].get_side(direction) == target:
				return
			tiles[idx].rotate()
		tiles[idx].flip()

def calibrate_first_corner(image_id, tiles):
	overlap = [i for i in tiles[image_id[0][0]].borders if i in tiles[image_id[0][1]].borders][1]
	calibrate_tile(tiles, image_id[0][0], overlap, "right")
	calibrate_tile(tiles, image_id[0][1], overlap, "left")

	overlap = [i for i in tiles[image_id[0][0]].borders if i in tiles[image_id[1][0]].borders]
	if overlap[0] == tiles[image_id[0][0]].data[0] or overlap[0] == tiles[image_id[0][0]].data[-1]:
		overlap = overlap[0]
	else:
		overlap = overlap[1]
	if overlap == tiles[image_id[0][0]].data[0]:
		tiles[image_id[0][0]].vflip()
		tiles[image_id[0][1]].vflip()
	calibrate_tile(tiles, image_id[1][0], overlap, "top")
	tiles[image_id[0][0]].calibrated = True
	tiles[image_id[0][1]].calibrated = True
	tiles[image_id[1][0]].calibrated = True

def calibrate_image(image_id, tiles):
	calibrate_first_corner(image_id, tiles)
	for y, row in enumerate(image_id):
		for x, idx in enumerate(row):
			if not tiles[idx].calibrated:
				if x == 0:
					calibrate_tile(tiles, idx, tiles[image_id[y - 1][x]].get_side("bot"), "top")
					tiles[idx].calibrated = True
				else:
					calibrate_tile(tiles, idx, tiles[image_id[y][x - 1]].get_side("right"), "left")
					tiles[idx].calibrated = True

def build_image(image_id, tiles, size):
	image = "Tile 0000:\n"
	for row in image_id:
		for y in range(size):
			for x in range(len(image_id)):
				image += "".join(tiles[row[x]].data[y])
			image += "\n"
	return Tile(image)

def snake_found(window):
	snake = [
		"                  # ",
		"#    ##    ##    ###",
		" #  #  #  #  #  #   "
	]
	for rs, rw in zip(snake, window):
		for s, w in zip(rs, rw):
			if s == '#' and w != '#':
				return False
	return True


def count_snakes(image):
	count = 0
	for transform in [	image.rotate, image.rotate, image.rotate, image.rotate,
						image.flip,
						image.rotate, image.rotate, image.rotate, image.rotate]:
		for y in range(len(image.data) - 2):
			for x in range(len(image.data[0]) - 19):
				if snake_found([s[x:x + 20] for s in image.data[y:y + 3]]):
					count += 1
		if count != 0:
			return count
		transform()
	return count
			

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n\n")
		
		pool = [Tile(line) for line in data]
		tiles = {tile.id: tile for tile in pool}
		links = generate_links(pool)

		image_id = build_image_id(links, int(len(pool) ** 0.5))
		calibrate_image(image_id, tiles)		
		for tile in tiles:
			tiles[tile].trim()

		image = build_image(image_id, tiles, 8)
		print(sum(row.count('#') for row in image.data) - count_snakes(image) * 15)