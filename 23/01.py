
class Cup:
	def __init__(self, p, l, n):
		self.prev = p
		self.label = l
		self.next = n
	
	def __repr__(self):
		return str(self.label)
	
	def __str__(self):
		return str(self.label)

def generate_cups(data):
	index = {}
	cups = []
	for i, v in enumerate(data):
		cups.append(Cup(i - 1, int(v), i + 1))
		index[int(v)] = i
	cups[0].prev = len(data) - 1
	cups[len(data) - 1].next = 0
	return index, cups

def wrap(n, h):
	return n - 1 if n - 1 > 0 else h

def simulate(cups, index, moves):
	curr = 0
	for i in range(moves):
		first = cups[curr].next
		second = cups[first].next
		third = cups[second].next

		cups[curr].next = cups[third].next
		cups[cups[third].next].prev = curr

		dest = wrap(cups[curr].label, len(cups))
		while dest in [cups[first].label, cups[second].label, cups[third].label]:
			dest = wrap(dest, len(cups))

		end = cups[index[dest]].next
		cups[index[dest]].next = first
		cups[first].prev = index[dest]
		cups[third].next = end
		cups[end].prev = third

		curr = cups[curr].next

def get_order(cups, index):
	curr = cups[cups[index[1]].next]
	s = ""
	for i in range(8):
		s += str(curr.label)
		curr = cups[curr.next]
	return s

if __name__ == "__main__":
	data = list("974618352")

	index, cups = generate_cups(data)
	simulate(cups, index, 100)
	print(get_order(cups, index))