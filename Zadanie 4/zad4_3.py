#4.3
def factorial(n):
	tmp = 1
	if n in (0,1):
		return 1
	else:
		for i in range(2, n+1):
			tmp = tmp * i
		return tmp
	
if __name__ == "__main__":
  print("Funkcja oblicza silnie")
  n = int(input("Podaj liczbe: "))
  print(factorial(n))