#3.9

#program zakłada, że podana liczba jest prawidłowa;
#program tłumaczy wszysktie możliwe poprawne liczby rzymskie na arabskie;
#zastosowałem słownik wybierający liczby na podstawie dopasowania z tabeli
#zawierającej możliwe kombinacje symboli rzymskich

def roman2int(tekst):
	D = {}
	D['I'] = 1
	D['II'] = 2
	D['III'] = 3
	D['IV'] = 4
	D['V'] = 5
	D['VI'] = 6
	D['VII'] = 7
	D['VIII'] = 8
	D['IX'] = 9
	D['X'] = 10
	D['XX'] = 20
	D['XXX'] = 30
	D['XL'] = 40
	D['L'] = 50
	D['LX'] = 60
	D['LXX'] = 70
	D['LXXX'] = 80
	D['XC'] = 90
	D['C'] = 100
	D['CC'] = 200
	D['CCC'] = 300
	D['CD'] = 400
	D['D'] = 500
	D['DC'] = 600
	D['DCC'] = 700
	D['DCCC'] = 800
	D['CM'] = 900
	D['M'] = 1000
	D['MD'] = 1500
	D['MM'] = 2000
	D['MMM'] = 3000


	wynik = 0
	tymczas = 0
	dl= len(tekst)
	i = 0
	s = ''
	while i<dl:
		s += tekst[i]
		if s in D:
			tymczas = D[s]
			i += 1
		else:
			wynik += tymczas
			s = ''		

	if s in D:
		wynik += D[s]
	return wynik

if __name__ == "__main__":
	while True:
		tekst = input("Podaj wartosc w systemie rzymskim: ")
		if tekst == 'stop': break
		x = roman2int(tekst)
		print("liczba w systemie arabskim: ", x)
