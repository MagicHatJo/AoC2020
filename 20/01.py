
class Tile:
	def __init__(self, data):
		data = data.split()
		self.id = int(data[1][:-1])
		self.data = [list(line) for line in data[2:]]		
		self.size = len(self.data)
		self.borders = self.get_borders()

	def rotate(self):
		for x in range(self.size // 2):
			for y in range(x, self.size - x - 1):
				self.data[x][y], self.data[y][self.size-1-x], self.data[self.size-1-x][self.size-1-y], self.data[self.size-1-y][x] = \
				self.data[y][self.size-1-x], self.data[self.size-1-x][self.size-1-y], self.data[self.size-1-y][x], self.data[x][y]

	def flip(self):
		self.data = [list(reversed(row)) for row in self.data]

	def get_borders(self):
		b = [self.data[0][:]]
		for transform in [self.rotate, self.rotate, self.rotate, self.flip, self.rotate, self.rotate, self.rotate]:
			transform()
			b.append(self.data[0][:])
		return b

	def __repr__(self):
		out = ""
		for row in self.data:
			for c in row:
				out += c
			out += "\n"
		return out

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n\n")
		
		pool = [Tile(line) for line in data]
		links = {tile: 0 for tile in pool}

		for i, first in enumerate(pool):
			for k, second in enumerate(pool):
				if i != k and any(j in first.borders for j in second.borders):
					links[first] += 1
		
		total = 1
		for tile in links:
			if links[tile] == 2:
				total *= tile.id
		print(total)