import random
import nltk

text = """Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.
In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.
"""
n = 2
ngrams = {}

#Creating the ngrams list
words = nltk.word_tokenize(text)
for i in range(len(words) - n):
	gram = ' '.join(words[i:i+n])
	if gram not in ngrams.keys():
		ngrams[gram] = [] 
	ngrams[gram].append(words[i+n])
# print (ngrams)


#tesing the Ngram
currentgram = ' '.join(words[0:n])
result = currentgram

for i in range(30):
	if currentgram not in ngrams.keys():
		break
	possibilities = ngrams[currentgram]
	nextitem = possibilities[random.randrange(len(possibilities))]
	result += ' '+nextitem
	rwords = nltk.word_tokenize(result)
	currentgram = ' '.join(rwords[len(rwords)-n: len(rwords)])

print (result)