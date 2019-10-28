#3.8
if __name__ == "__main__":
	t = [0,1,2,3,4]
	print("Lista pierwsza:")
	print(t)

	e = [1, 'a', 'b','c', 'd']
	print("Lista druga:")
	print(e)

	lista = list(set(t).intersection(set(e)))
	print("Lista wystepujacych w obu:")
	print(lista)

	lista = list(set(e + t))
	print("Lista wszystkich elementow:")
	print(lista)