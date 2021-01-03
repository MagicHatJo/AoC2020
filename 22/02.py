
def play_game(p1, p2):
	seen = set()
	while p1 and p2:
		h = hash(str(p1) + str(p2))
		if h in seen:
			return 1, p1
		seen.add(h)
		
		t1 = p1.pop(0)
		t2 = p2.pop(0)

		if t1 <= len(p1) and t2 <= len(p2):
			winner, _ = play_game(p1[:t1], p2[:t2])
		else:
			winner = 1 if t1 > t2 else 2

		if winner == 1:
			p1.extend([t1, t2])
		else:
			p2.extend([t2, t1])
	return (1, p1) if p1 else (2, p2)

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n\n")

		p1 = [int(i) for i in data[0].split("\n")[1:]]
		p2 = [int(i) for i in data[1].split("\n")[1:]]
		
		_, winning_deck = play_game(p1, p2)
		print(sum([v * (len(winning_deck) - i) for i, v in enumerate(winning_deck)]))