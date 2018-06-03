
import json
from difflib import get_close_matches 

data = json.load(open('data.json','r'))

def find_meaning(word):
	if word.lower() in data:
		return data[word.lower()]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word.lower(), data.keys())) > 0:
		ch = raw_input('Did you mean %s instead? Press Y if Yes, N if No: '%get_close_matches(word.lower(),data.keys())[0])
		if ch == 'Y' or ch == 'y':
			return data[get_close_matches(word.lower(),data.keys())[0]]
		else:
			return ('The word does not exist.')
	else:
		return('The word does not exist.')

word = raw_input('Enter a word: ')

opt = find_meaning(word)

if type(opt) == list:
	count = 1
	for line in opt:
		print('{}. {}'.format(count,line))
		count += 1
else:
	print(opt)
