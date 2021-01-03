
if __name__ == "__main__":
	card_pub_key = 13233401
	door_pub_key = 6552760

	i = 1
	itr = 0
	while i != door_pub_key:
		i = i * 7 % 20201227
		itr += 1

	print(pow(card_pub_key, itr, 20201227))