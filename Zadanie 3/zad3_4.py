#3.4
if __name__ == "__main__":
	while True:
		try:
			l = input("Podaj liczbe: ")
			x = float(l)
			print('podana liczba: ' + str(x) + ', 3-cia potęga: ' + str(pow(x, 3)))
			
		except ValueError:
			if(l == 'stop'): break;
			print('To nie jest liczba! Podaj liczbe')