import sys
import random
from collections import defaultdict


def markov(input):
	with open(input, 'r') as file:
		data = file.read().replace('\n', '')
	data_split = data.split()
	markov_dict = defaultdict()
	for i in range(2, len(data_split)):
		if (data_split[i-2], data_split[i-1]) not in markov_dict.keys():
			markov_dict[(data_split[i-2], data_split[i-1])] = [data_split[i]]
		else:
			markov_dict[(data_split[i-2], data_split[i-1])].append(data_split[i])
	return markov_dict

def generate_sentence(markov_dict, num_words):
	'''
	markov_dict: input dictionary of a parsed text file
	num_words: number of words that the output sentence should have
	'''
	# Start with capitalized words and without a period after the word
	start = [key for key in markov_dict.keys() if key[0][0].isupper() and key[0][-1] != '.']
	# Select starting word pair randomly
	start_list = list(random.choice(start))
	# Further add words randomly to the sentence
	while len(start_list) < num_words:
		try:
			# Take the 2 prior words as keys and look which word follows
			start_list.append(random.choice(markov_dict[(start_list[-2], start_list[-1])]))
		except KeyError:
			start_list += list(random.choice(markov_dict.keys()))
	print(' '.join(start_list))

if __name__ == '__main__':
	markov_dict = markov(sys.argv[1])
	generate_sentence(markov_dict, int(sys.argv[2]))

# output: Their heads were the most foolish-looking things you ever saw, and they say under the sea lions keep themselves to themselves."Scoochnie! Ochen scoochnie!" ("I'm lonesome, very lonesome!") said Kotick. "Good sport, gentlemen?" The big things answered by bowing and waving
