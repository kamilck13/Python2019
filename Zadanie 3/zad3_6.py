#3.6
def rysuj_kratke(dlugosc, wysokosc):
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
	print("Program rysuje siatke")
	x = int(input("Podaj wartosc x: "))
	y = int(input("Podaj wartosc y: "))

	s = rysuj_kratke(x, y)
	print(s)