
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

def validate(message, to_match, rules, memo = {}):
	if (message, to_match) not in memo:
		if type(rules[to_match]) == str:
				result = message == rules[to_match]
		elif to_match == 8 or to_match == 11:
			if len(message) % 8:
				result = False
			else:
				result = True
				for i in range(0, len(message) // (1 + (to_match == 11)), 8):
					if not validate(message[i:i + 8], 42, rules, memo):
						result = False
						break
					if to_match == 11:
						for i in range(len(message) // 2, len(message), 8):
							if not validate(message[i:i + 8], 31, rules, memo):
								result = False
								break
		else:	
			for rule in rules[to_match]:
				if len(rule) == 1:
					result = validate(message, rule[0], rules, memo)
				else:
					result = False
					for i in range(1, len(message)):
						if (validate(message[:i], rule[0], rules, memo) and
							validate(message[i:], rule[1], rules, memo)):
							result = True
							break
				if result:
					break
		memo[message, to_match] = result
	return memo[message, to_match]

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.read().split("\n\n")
		rules = parse_rules(data[0].split('\n'))
		rules[8].add((42, 8))
		rules[11].add((42, 11, 31))
		messages = data[1].split('\n')
		memo = {}
		print(sum([validate(s, 0, rules, memo) for s in messages]))