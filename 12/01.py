#!/usr/bin/python3

class Ship:

	def __init__(self):
		self.pos = complex(0)
		self.dir = complex(1, 0)

		self.cmd = {
			'N': lambda v: (self.pos + (v * complex(0, 1)), self.dir),
			'S': lambda v: (self.pos - (v * complex(0, 1)), self.dir),
			'E': lambda v: (self.pos + v, self.dir),
			'W': lambda v: (self.pos - v, self.dir),
			'L': lambda v: (self.pos, self.dir * (complex(0, 1) ** (v // 90))),
			'R': lambda v: (self.pos, self.dir * ((-complex(0, 1)) ** (v // 90))),
			'F': lambda v: (self.pos + (self.dir * v), self.dir)
		}

	def move(self, data):
		for line in data:
			self.pos, self.dir = self.cmd[line[0]](int(line[1:]))
		return (self.pos.real, self.pos.imag)

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		x, y = Ship().move(data)
		print(int(abs(x) + abs(y)))