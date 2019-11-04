#4.4
def fibonacci(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a

if __name__ == "__main__":
  print("Funkcja oblicza n-ty wyraz ciągu fibonacziego")
  n = int(input("Podaj liczbe: "))
  print(fibonacci(n))