#!/usr/bin/python3

def earliest_bus(start_time, id_list):
	closest_times = [i - start_time % i for i in id_list]
	i = closest_times.index(min(closest_times))
	return id_list[i] * closest_times[i]

if __name__ == "__main__":
	with open("input", 'r') as f:
		data = f.readlines()
		start_time = int(data[0])
		id_list = [int(i) for i in data[1].split(',') if i != 'x']
		print(earliest_bus(start_time, id_list))