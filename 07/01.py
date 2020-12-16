#!/usr/bin/python3

def generate_graph():
	graph = {}

	for line in data:
		line = line.split()
		key = line[0] + line[1]
		graph[key] = []
		if len(line) != 7:
			for i in range(4, len(line), 4):
				graph[key].append(line[i + 1] + line[i + 2])
	return graph

def count_shiny(graph):
	count = 0

	for key in graph:
		queue = graph[key]
		for child in queue:
			if child == "shinygold":
				count += 1
				break
			queue += graph[child]
	
	return count

if __name__ == "__main__":
	with open("input") as f:
		data = [line.strip() for line in f]
		print(count_shiny(generate_graph()))

