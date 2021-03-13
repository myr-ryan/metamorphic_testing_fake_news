# coding=utf-8
#import spacy
import numpy as np
import pandas as pd
from functions import *

def MR_2(browser):
	metamorphic_testing(browser, '../reason_lists.csv', '../antonymy.csv')
	# nlp = spacy.load('en_core_web_sm')
	# all_sentences = []

	# for i in range(len(sentences)):
	# 	print('Processing index ', i)
	# 	new_sentences = ''

	# 	sentence = sentences[i].split('\n')
	# 	for s in sentence:

	# 		doc = nlp(s)
	# 		tokens = [token for token in doc]
	# 		# 'pos' stands for part-of-speech tagging, verb, noun or adj, etc
	# 		pos = [token.pos_ for token in doc]
	# 		# 'dep' stands for dependency parsing, nounsubject, determiner, etc
	# 		dep = [token.dep_ for token in doc]
			
	# 		# count the number of noun subjects
	# 		num_of_subj = dep.count('nsubj')
	# 		# count the number of verbs
	# 		num_of_verbs = pos.count('VERB')

	# 		new_s = ''
	# 		if (num_of_verbs != 0) and (num_of_subj != 0):
	# 			first_verb = pos.index('VERB')
	# 			first_subj = dep.index('nsubj')
	# 			# antonymy only if the subjects are next to the verbs
	# 			if (first_verb - first_subj) <= 2:
	# 				words_in_a_sentence = s.split(' ')			
	# 				j = 0
	# 				for w in words_in_a_sentence:
	# 					if j == first_subj - 1:
	# 						new_s = new_s + w
	# 						new_s = new_s + ' '
	# 						new_s = new_s + 'not '
	# 					else:
	# 						new_s = new_s + w
	# 						new_s = new_s + ' '	
	# 					j += 1		
	# 			else:
	# 				new_s = s
	# 		else:
	# 			new_s = s

	# 		new_sentences = new_sentences + new_s + '\n'
	# 	# eliminate the last space using rstrip()
	# 	new_sentences = new_sentences.rstrip()
	# 	if sentences[i] == new_sentences:
	# 		print(new_sentences)
	# 		print()
	# 		print('No antonymy was applied, index ', i)
	# 		print(sentences[i])
	# 	all_sentences.append(new_sentences)


	# final = pd.DataFrame({
	# 	'Antonymy sentences': all_sentences,
	# 	'Labels': np.nan
	# 	})
	# final.to_csv('../antonymy5000.csv', encoding='utf-8')

	


				

		


			