#!/usr/bin/python3

class Ship:

	def __init__(self):
		self.pos = complex(0)
		self.wp = complex(10, 1)

		self.cmd = {
			'N': self.north,
			'S': self.south,
			'E': self.east,
			'W': self.west,
			'L': self.left,
			'R': self.right,
			'F': self.forward
		}

	def move(self, data):
		for line in data:
			act = line[0]
			val = int(line[1:])
			self.cmd[act](val)
		return (self.pos.real, self.pos.imag)

	def north(self, val):
		self.wp += val * complex(0, 1)
	
	def south(self, val):
		self.wp -= val * complex(0, 1)

	def east(self, val):
		self.wp += val
	
	def west(self, val):
		self.wp -= val

	def left(self, val):
		self.wp *= complex(0, 1) ** (val // 90)
	
	def right(self, val):
		self.wp *= (-complex(0, 1)) ** (val // 90)

	def forward(self, val):
		self.pos += self.wp * val

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		ship = Ship()
		x, y = ship.move(data)
		print(int(abs(x) + abs(y)))