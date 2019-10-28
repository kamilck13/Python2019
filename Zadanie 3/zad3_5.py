#3.5
if __name__ == "__main__":
	n = int(input("Podaj dlugosc miarki: "))
	s = '|'
	for x in range(n):
		s += '....|'
		x = x + 1
	s += '\n0'
	for x in range(n):
		next_x = x + 1
		x = str(next_x)
		next_x = len(x)
		while (5 - next_x):
			s += ' '
			next_x += 1
		s += x
	print(s)