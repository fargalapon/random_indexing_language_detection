# random_idx.py
# creates random index vectors for a number of languages

# libraries
import numpy as np
import string
import utils

# constants
alphabet = string.lowercase
M = 26 # latin letters

# to be parametrized later!
N = 1000 # dimension of random index vectors
k = 10 # number of + (or -)
languages = ['english','german','norwegian']

num_lang = len(languages) # english, german, norwegian (in this order)

# build row-wise k-sparse random index matrix
# each row is random index vector for letter
RI = np.zeros((26,N))
for i in xrange(26):
		rand_idx = np.random.permutation(N)
		RI[i,rand_idx[0:k]] = 1
		RI[i,rand_idx[k:2*k]] = -1

lang_vectors = np.zeros((num_lang,N))
for i in xrange(num_lang):
		print "processing " + str(languages[i])
		# load text one at a time (to save mem), English, German, Norwegian
		# as list, text_list = [english_text, german_text, ..., norwegian_text]
		lang_text = utils.load_lang(languages[i])
		for letter in lang_text:
				letter_idx = alphabet.find(letter)
				lang_vectors[i,:] += RI[letter_idx,:]