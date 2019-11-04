#3.5
def miarka():
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
	return s


#3.6
def rysuj_kratke():
	dlugosc = int(input("Podaj wartosc x: "))
	wysokosc = int(input("Podaj wartosc y: "))
	s = ''
	for x in range(wysokosc):
		s += linia_z_plusami(dlugosc)
		s += linia_ze_spacjami(dlugosc)
	s += linia_z_plusami(dlugosc)
	return s

def linia_z_plusami(dlugosc):
	s = '+'
	for x in range(dlugosc):
		s += '---+'
	return s + '\n'
	
def linia_ze_spacjami(dlugosc):
	s = '|'
	for x in range(dlugosc):
		s += '   |'
	return s + '\n'

if __name__ == "__main__":
	print(miarka())
	print(rysuj_kratke())
