phrase = "She sells, sea shells on the sea shore. Sea shells on the sea shore are really beautiful"
words = phrase.lower().replace('.','').replace(',','').split()
unique_words = {word for word in words}
print(unique_words)