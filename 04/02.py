#!/usr/bin/python3

import string

with open("input") as f:
	data = f.read().split("\n\n")

	count = 0
	for line in data:
		d = {}
		info = line.split()
		for pair in info:
			d[pair[0:3]] = pair[4:]

		count += (	("byr" in d and d["byr"].isdigit() and len(d["byr"]) == 4 and (1920 <= int(d["byr"]) <= 2002)) and
					("iyr" in d and d["iyr"].isdigit() and len(d["iyr"]) == 4 and (2010 <= int(d["iyr"]) <= 2020)) and
					("eyr" in d and d["eyr"].isdigit() and len(d["eyr"]) == 4 and (2020 <= int(d["eyr"]) <= 2030)) and
					(("hgt" in d and ((d["hgt"][-2:] == "cm" and (150 <= int(d["hgt"][:-2]) <= 193)) or (d["hgt"][-2:] == "in" and (59 <= int(d["hgt"][:-2]) <= 76))))) and
					("hcl" in d and d["hcl"][0] == '#' and len(d["hcl"]) == 7 and set(d["hcl"][1:]).issubset(string.hexdigits)) and
					("ecl" in d and d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and
					("pid" in d and d["pid"].isdigit() and len(d["pid"]) == 9))

	print(count)