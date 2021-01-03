
def parse_data(data):
	allergens = {}

	for d in data:
		w, a = d.split(" (contains ")
		w = w.split()

		for allergen in a.strip()[:-1].split(", "):
			if allergen in allergens:
				allergens[allergen].intersection_update(w)
			else:
				allergens[allergen] = set(w)

	return allergens

def match_ingredients(allergens):
	
	def remove(allergens, ingredient):
		for a in allergens:
			if len(allergens[a]) > 1 and ingredient in allergens[a]:
				allergens[a].remove(ingredient)

	while any([len(i) > 1 for i in allergens.values()]):
		for a in allergens:
			if len(allergens[a]) == 1:
				remove(allergens, *allergens[a])

	return allergens

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		match_ingredients(parse_data(data))
		print(",".join([allergens[k].pop() for k in sorted(allergens.keys())]))
		