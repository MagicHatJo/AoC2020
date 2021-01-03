
def play_game(p1, p2):
	while p1 and p2:
		t1 = p1.pop(0)
		t2 = p2.pop(0)
		if t1 > t2:
			p1.extend([t1, t2])
		else:
			p2.extend([t2, t1])
	return p1 if p1 else p2

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n\n")

		p1 = [int(i) for i in data[0].split("\n")[1:]]
		p2 = [int(i) for i in data[1].split("\n")[1:]]
		
		winning_deck = play_game(p1, p2)
		print(sum([v * (len(winning_deck) - i) for i, v in enumerate(winning_deck)]))