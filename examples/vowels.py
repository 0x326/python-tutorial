def iterative(word):
	total = 0
	for letter in word:
		if letter in 'aeiouAEIOU':
			total += 1
	return total


def recursive(word):
	if len(word) == 0:
		return 0
	if word[0] in 'aeiouAEIOU':
		return 1 + recursive(word[1:])
	else:
		return recursive(word[1:])


def pythonic(word):
	return sum([1 for letter in word if letter in 'aeiouAEIOU'])
