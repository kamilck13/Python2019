if __name__ == "__main__":
#3.1
	x = 2
	y = 3
	if (x > y):
	    result = x
	else:
	    result = y
#	powyższy kod jest poprawny

#	for i in "qwerty": if ord(i) < 100: print (i)
#	powyżysz kod nie jest poprawny, powinien wygładać tak:
	for i in "qwerty":
		if ord(i) < 100:
			print (i)

	for i in "axby": print (ord(i)) if ord(i) < 100 else i
#	powyższy kod jest poprawny

#3.2
	L = [3, 5, 4]
	L = L.sort()

	#x, y = 1, 2, 3
	#poprawnie
	x, y, z = 1, 2, 3

	X = 1, 2, 3
	#cyfry trzeba zapisać w nawiasach kwadratowych
	X = [1, 2, 3]
	X[1] = 4

	X = [1, 2, 3]
	#X[3] = 4 - wykraczamy poza indeks bo liczymy od 0

	X = "abc"
	#X.append("d") - napis nie posiada metody append
	X += "d"

	#map(pow, range(8))
	#poprawnie:
	map(lambda x: pow(x,2), range(8))

