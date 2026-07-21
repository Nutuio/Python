phrase = "The cat is in the hut. The bug is under the table. You must buy a pair of new shoe before the annual day"
words = phrase.lower().replace('.', '').replace(',', '').split()
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}
print(consonants)