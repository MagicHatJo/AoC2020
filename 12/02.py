#!/usr/bin/python3

class Ship:

	def __init__(self):
		self.pos = complex(0)
		self.wp = complex(10, 1)

		self.cmd = {
			'N': lambda v: (self.pos, self.wp + (v * (complex(0, 1)))),
			'S': lambda v: (self.pos, self.wp - (v * (complex(0, 1)))),
			'E': lambda v: (self.pos, self.wp + v),
			'W': lambda v: (self.pos, self.wp - v),
			'L': lambda v: (self.pos, self.wp * (complex(0, 1) ** (v // 90))),
			'R': lambda v: (self.pos, self.wp * ((-complex(0, 1)) ** (v // 90))),
			'F': lambda v: (self.pos + (self.wp * v), self.wp)
		}

	def move(self, data):
		for line in data:
			self.pos, self.wp = self.cmd[line[0]](int(line[1:]))
		return (self.pos.real, self.pos.imag)

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		x, y = Ship().move(data)
		print(int(abs(x) + abs(y)))