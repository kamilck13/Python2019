#2.10
def numberOfWords(line):
	return len(line.split())

#2.11
def insertUnderscore(word):
	return "_".join(list(word))

#2.12
def firstChar(line):
	znaki = [x[0] for x in line.split()]
	return "".join(znaki)

def lastChar(line):
	znaki = [x[-1] for x in line.split()]
	return "".join(znaki)

#2.13
def numberOfChars(line):
	return sum(len(x) for x in line.split())

#2.14
def theLongestWord(line):
	w = line.split()
	w.sort(key = len)
	return w[-1]

#2.15
def LengthOfTheLongestWord(line):
	return len(theLongestWord(line))

#2.15
def WordOfList(L):
	return "".join(str(x) for x in L)

#2.16
def replaceWord(line):
	return line.replace("GvR", "Guido van Rossum")

#2.17
def lexicographicalSorting(line):
	w = line.split()
	w.sort()
	return w	

def sortingByLength(line):
	w = line.split()
	w.sort(key = len)
	return w

#2.18
def numberOfZeros(number):
	return str(number).count('0')

#2.19
def paddingWithZeros(L):
	return ",".join([str(x).zfill(3) for x in L])

if __name__ == "__main__":
	line = "To\njest napis\twielowierszowy GvR"
	word = "taki napis"
	L = [1, 2, 33, 444, 12, 99, 5]
	number = 12010129405000

	assert numberOfWords(line) == 5
	assert insertUnderscore(word) == "t_a_k_i_ _n_a_p_i_s"
	assert firstChar(line) == "TjnwG"
	assert lastChar(line) == "otsyR"
	assert numberOfChars(line) == 28
	assert theLongestWord(line) == "wielowierszowy"
	assert LengthOfTheLongestWord(line) == 14
	assert WordOfList(L) == "123344412995"
	assert replaceWord(line) == "To\njest napis\twielowierszowy Guido van Rossum"
	assert lexicographicalSorting(line) == ['GvR', 'To', 'jest', 'napis', 'wielowierszowy']
	assert sortingByLength(line) == ['To', 'GvR', 'jest', 'napis', 'wielowierszowy']
	assert numberOfZeros(number) == 6
	assert paddingWithZeros(L) == "001,002,033,444,012,099,005"