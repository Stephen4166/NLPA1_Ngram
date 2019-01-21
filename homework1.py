import sys
import nltk
import re

# read in and preprocess
file = open(sys.argv[1], 'r', encoding='utf-8')
text = file.read()
file.close()
sent_tokenize_list = nltk.sent_tokenize(text)
tokens = []
for sent in sent_tokenize_list:
    tokens.extend(nltk.word_tokenize(sent))
tokens[0] = 'Apple'
for i in range(len(tokens)):
    tokens[i] = tokens[i].lower()

# make the freq dict
freq = {}
for token in tokens:
    if token in freq:
        freq[token] += 1
    else:
        freq[token] = 1
V = len(freq)
N = len(tokens)

sent1 = sys.argv[2]
sent2 = sys.argv[3]

# --------------------------------------------------------------------------------------------
# tokenize sentence1
words1 = nltk.word_tokenize(sent1)
for i in range(len(words1)):
    words1[i] = words1[i].lower()
words1[:] = [word for word in words1 if not re.match("\.", word)]
l1 = words1[:]
new_words1 = list(set(words1))
new_words1.sort(key=words1.index)
words1 = new_words1

# bigram count of the first sentence
dict1 = {}
for word in words1:
    if word not in dict1:
        dict1[word] = []
for word in words1:
    for i in range(len(dict1)):
        dict1[word].append(0)
for i in range(len(tokens)-1):
    pointer = tokens[i]
    nextOne = tokens[i+1]
    if pointer in words1 and nextOne in words1:
        dict1[pointer][words1.index(nextOne)] += 1

# sentence1 smoothing counts
dict1b = {}
for key in dict1:
    dict1b[key] = dict1[key][:]
    dict1b[key] = [x+1 for x in dict1b[key]]

# bigram probabilities of the first sentence
pdict1 = {}
for key in dict1:
    pdict1[key] = dict1[key][:]
    pdict1[key] = [x/freq[key] for x in pdict1[key]]

# sentence1 smoothing probabilities
pdict1b = {}
for key in dict1b:
    pdict1b[key] = dict1b[key][:]
    pdict1b[key] = [x/(freq[key]+V) for x in pdict1b[key]]

# -------------------------------------------------------------------------------------------
# tokenize sentence2
words2 = nltk.word_tokenize(sent2)
for i in range(len(words2)):
    words2[i] = words2[i].lower()
words2[:] = [word for word in words2 if not re.match("\.", word)]
l2 = words2[:]
new_words2 = list(set(words2))
new_words2.sort(key=words2.index)
words2 = new_words2

# bigram count of the first sentence
dict2 = {}
for word in words2:
    if word not in dict2:
        dict2[word] = []
for word in words2:
    for i in range(len(dict2)):
        dict2[word].append(0)
for i in range(len(tokens)-1):
    pointer = tokens[i]
    nextOne = tokens[i+1]
    if pointer in words2 and nextOne in words2:
        dict2[pointer][words2.index(nextOne)] += 1

# sentence2 smoothing counts
dict2b = {}
for key in dict2:
    dict2b[key] = dict2[key][:]
    dict2b[key] = [x+1 for x in dict2b[key]]

# bigram probabilities of the first sentence
pdict2 = {}
for key in dict2:
    pdict2[key] = dict2[key][:]
    pdict2[key] = [x/freq[key] for x in pdict2[key]]

# sentence1 smoothing probabilities
pdict2b = {}
for key in dict2b:
    pdict2b[key] = dict2b[key][:]
    pdict2b[key] = [x/(freq[key]+V) for x in pdict2b[key]]


# ------------------------------------------------------------------------------------------------------
# print the results
print("A ------------------------------Bigram Counts--------------------------------------------------")
print("i ------------------------------No Smoothing-------------------------------------------")
print("Sentence1: ")
print(''.ljust(12), end='')
for word in words1:
    print(str(word).ljust(12), end='')
print()
for word in words1:
    print(word.ljust(12), end='')
    for item in dict1[word]:
        print(str(item).ljust(12), end='')
    print()
print()

print("Sentence2: ")
print(''.ljust(12), end='')
for word in words2:
    print(str(word).ljust(12), end='')
print()
for word in words2:
    print(word.ljust(12), end='')
    for item in dict2[word]:
        print(str(item).ljust(12), end='')
    print()
print()

print("ii ------------------------------With Smoothing-------------------------------------------")
print("Sentence1: ")
print(''.ljust(12), end='')
for word in words1:
    print(str(word).ljust(12), end='')
print()
for word in words1:
    print(word.ljust(12), end='')
    for item in dict1b[word]:
        print(str(item).ljust(12), end='')
    print()
print()

print("Sentence2: ")
print(''.ljust(12), end='')
for word in words2:
    print(str(word).ljust(12), end='')
print()
for word in words2:
    print(word.ljust(12), end='')
    for item in dict2b[word]:
        print(str(item).ljust(12), end='')
    print()
print()

print("B ------------------------------Bigram Probabilities--------------------------------------------------")
print("i ------------------------------No Smoothing-------------------------------------------")
print("Sentence1: ")
print(''.ljust(12), end='')
for word in words1:
    print("%-12s" % word, end='')
print()
for word in words1:
    print("%-12s" % word, end='')
    for item in pdict1[word]:
        print("%-12.6f" % item, end='')
    print()
print()

print("Sentence2: ")
print(''.ljust(12), end='')
for word in words2:
    print("%-12s" % word, end='')
print()
for word in words2:
    print("%-12s" % word, end='')
    for item in pdict2[word]:
        print("%-12.6f" % item, end='')
    print()
print()

print("ii ------------------------------With Smoothing-------------------------------------------")
print("Sentence1: ")
print(''.ljust(12), end='')
for word in words1:
    print("%-12s" % word, end='')
print()
for word in words1:
    print("%-12s" % word, end='')
    for item in pdict1b[word]:
        print("%-12.6f" % item, end='')
    print()
print()

print("Sentence2: ")
print(''.ljust(12), end='')
for word in words2:
    print("%-12s" % word, end='')
print()
for word in words2:
    print("%-12s" % word, end='')
    for item in pdict2b[word]:
        print("%-12.6f" % item, end='')
    print()
print()

print("C ------------------------------Total Probabilities--------------------------------------------------")
print("i ------------------------------No Smoothing-------------------------------------------")
print("Sentence1: ")
head = l1[0]
p1 = freq[head] / N
for i in range(1, len(l1)):
    pointer = l1[i-1]
    p1 *= pdict1[pointer][words1.index(l1[i])]
print(p1)
print()

print("Sentence2: ")
head = l2[0]
p2 = freq[head] / N
for i in range(1, len(l2)):
    pointer = l2[i-1]
    p2 *= pdict2[pointer][words2.index(l2[i])]
print(p2)
print()

print("ii ------------------------------With Smoothing-------------------------------------------")
print("Sentence1: ")
head = l1[0]
p1 = (freq[head]+1) / (N+V)
for i in range(1, len(l1)):
    pointer = l1[i-1]
    p1 *= pdict1b[pointer][words1.index(l1[i])]
print(p1)
print()

print("Sentence2: ")
head = l2[0]
p2 = (freq[head]+1) / (N+V)
for i in range(1, len(l2)):
    pointer = l2[i-1]
    p2 *= pdict2b[pointer][words2.index(l2[i])]
print(p2)
print()
print("From the results, we know that the first sentence is more probable.")