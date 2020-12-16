#!/usr/bin/python3

def generate_graph():
	graph = {}

	for line in data:
		line = line.split()
		key = line[0] + line[1]
		graph[key] = []
		if len(line) != 7:
			for i in range(4, len(line), 4):
				graph[key].append((int(line[i]), line[i + 1] + line[i + 2]))
	return graph

def count_individual(node, graph, memo):
	count = 0

	for child in graph[node]:
		if child[1] not in memo:
			memo[child[1]] = count_individual(child[1], graph, memo) + 1
		count += child[0] * memo[child[1]]
	return count

if __name__ == "__main__":
	with open("input") as f:
		data = [line.strip() for line in f]
		print(count_individual("shinygold", generate_graph(), {}))