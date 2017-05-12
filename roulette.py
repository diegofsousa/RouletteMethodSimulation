import random

def roulette(prepositions):
	list_drawn = list()
	map_prepositions = list()
	for i in prepositions:
		for a in range(i[1]):
			map_prepositions.append(i[0])

	q_aux = list()

	while len(map_prepositions) != 0:
		print(map_prepositions)
		new_key_drawn = random.choice(map_prepositions)
		list_drawn.append(new_key_drawn)
		for o in range(len(map_prepositions)):
			if map_prepositions[o] == new_key_drawn:q_aux.append(o)
		del(map_prepositions[q_aux[0]:q_aux[-1]+1])
		q_aux.clear()

	print(list_drawn)	

a = [['a',50], ['b',30], ['c', 20]]

print(a)
roulette(a)