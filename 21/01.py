
def parse_data(data):
	ingredients = {}
	unsafe = set()
	allergens = {}

	for d in data:
		w, a = d.split(" (contains ")
		w = w.split()
		for word in w:
			ingredients[word] = ingredients.get(word, 0) + 1

		for allergen in a.strip()[:-1].split(", "):
			if allergen in allergens:
				allergens[allergen].intersection_update(w)
			else:
				allergens[allergen] = set(w)
	
	for a in allergens.values():
		unsafe.update(a)

	return ingredients, unsafe

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		ingredients, unsafe = parse_data(data)
		print(sum([ingredients[i] for i in ingredients if i not in unsafe]))