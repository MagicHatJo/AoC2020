
def parse_rules(data):
	rules = {}
	for line in data:
		n, r = line.split(": ")
		if r[0] == "\"":
			r = r[1]
		else:
			r = set(map(lambda x: tuple(map(int, x.split())), r.split(" | ")))
		rules[int(n)] = r
	return rules

def valid_matches(to_match, rules, memo = {}):
	if to_match not in memo:
		result = set()
		if type(rules[to_match]) == str:
			result.add(rules[to_match])
		else:
			for rule in rules[to_match]:
				if len(rule) == 1:
					result |= valid_matches(rule[0], rules, memo)
				else:
					for start in valid_matches(rule[0], rules, memo):
						for end in valid_matches(rule[1], rules, memo):
							result.add(start + end)
		memo[to_match] = result
	return memo[to_match]

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n\n")
		rules = parse_rules(data[0].split('\n'))
		messages = data[1].split('\n')
		valid = valid_matches(0, rules)
		print(sum([s in valid for s in messages]))