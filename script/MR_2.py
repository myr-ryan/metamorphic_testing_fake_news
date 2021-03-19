# coding=utf-8
import spacy
import numpy as np
import pandas as pd
from functions import *
import string

def MR_2(sentences, labels):
	#metamorphic_testing(browser, '../reason_lists.csv', '../antonymy.csv')
	nlp = spacy.load('en_core_web_sm')
	all_sentences = []

	for i in range(len(sentences)):
		#print('Processing index ', i)
		new_sentences = ''

		sentence = sentences[i].split('\n')
		for s in sentence:
			s = s[1:-1]

			s = "He is taking it away."

			doc = nlp(s)
			tokens = [token for token in doc]
			# 'pos' stands for part-of-speech tagging, verb, noun or adj, etc
			pos = [token.pos_ for token in doc]
			# 'dep' stands for dependency parsing, nounsubject, determiner, etc
			dep = [token.dep_ for token in doc]
			
			# count the number of noun subjects
			num_of_subj = dep.count('nsubj')
			# count the number of verbs
			num_of_verbs = pos.count('VERB')

			new_s = ''
			if (num_of_verbs != 0) and (num_of_subj != 0):
				first_verb = pos.index('VERB')
				first_subj = dep.index('nsubj')
				# antonymy only if the subjects are next to the verbs
				# allows for subject, 'have' or 'will', adverb, verb
				if ((first_verb - first_subj) > 0) and ((first_verb - first_subj) <= 3):
					#words_in_a_sentence = str(doc).split(' ')
					words_in_a_sentence	= [str(token) for token in doc]	
					j = 0
					lemma = False
					is_add_not = False
					has_quotation = False
					#delete_not = False
					nonverb_lemma = False

					for w in words_in_a_sentence:
						#print(w)
						if j == first_subj:

							original_verb = doc[first_verb].lemma_
							# print(str(original_verb))
							# print(str(doc[first_verb]))
							# if the morphology is the same
							if str(original_verb) == str(doc[first_verb]):
								if (str(doc[j + 1]) == 'will') or (str(doc[j + 1]) == 'shall') or (str(doc[j + 1]) == 'can') or (str(doc[j + 1]) == 'should') \
									or (str(doc[j + 1]) == 'could') or (str(doc[j + 1]) == 'have') or (str(doc[j + 1]) == 'has') or (str(doc[j + 1]) == 'had') \
									or (str(doc[j + 2]) == 'have') or (str(doc[j + 2]) == 'has') or (str(doc[j + 2]) == 'had') \
									or (str(doc[j + 2]) == 'will') or (str(doc[j + 2]) == 'shall') or (str(doc[j + 2]) == 'can') or (str(doc[j + 2]) == 'should') or (str(doc[j + 2]) == 'could'):
									if (str(doc[j + 2]) == 'not') or (str(doc[j + 2]) == 'n\'t'):
										new_s = new_s + ' ' + str(doc[first_subj])
										delete_not = True
									else:
										new_s = new_s + ' ' + str(doc[first_subj])
										is_add_not = True
									#j += 2
								# elif (str(doc[j + 1]) == 'won\'t') or (str(doc[j + 1]) == 'shouldn\'t') or (str(doc[j + 1]) == 'can\'t') or (str(doc[j + 1]) == 'couldn\'t') \
								# 	or (str(doc[j + 2]) == 'won\'t') or (str(doc[j + 2]) == 'shouldn\'t') or (str(doc[j + 2]) == 'can\'t') or (str(doc[j + 2]) == 'couldn\'t'):
								elif (str(doc[j + 1]) == 'n\'t') or (str(doc[j + 2]) == 'n\'t'):
									new_s = new_s + ' ' + str(doc[first_subj])
								# elif (str(doc[j + 1]) == 'not') or (str(doc[j + 2]) == 'not'):
								# 	new_s = new_s + ' ' + str(doc[first_subj])
								# 	delete_not = True
								else:
									new_s = new_s + ' ' +str(doc[first_subj]) + ' don\'t'
									lemma = True
									#j += 1
							# if the morphology is not the same
							else:
								if (str(doc[j + 1]) == 'have') or (str(doc[j + 1]) == 'has') or (str(doc[j + 1]) == 'had') \
									or (str(doc[j + 2]) == 'have') or (str(doc[j + 2]) == 'has') or (str(doc[j + 2]) == 'had'):
									new_s = new_s + ' ' + str(doc[first_subj])
									is_add_not = True
									#j += 2
								elif ((str(original_verb[-1]) == 's') and (str(doc[first_verb])[-1] == 'es')) or ((str(original_verb[-1]) != 's') and (str(doc[first_verb])[-1] == 's')):
									new_s = new_s + ' ' + str(doc[first_subj]) + ' doesn\'t'
									lemma = True
									#j += 1
								else:
									new_s = new_s + ' ' + str(doc[first_subj]) + ' did\'t'
									lemma = True
									#j += 1
						
						elif j == first_verb:
							if lemma or nonverb_lemma:
								new_s = new_s + ' ' + str(doc[j].lemma_)
								#j += 1
							elif is_add_not:
								new_s = new_s + ' not ' + w
								#j += 1

							else:
								new_s = new_s + ' ' + w
								#j += 1

						else:
							if str(doc[j]) in string.punctuation:
								new_s = new_s + w
							elif (str(doc[j]) == 'not') or (str(doc[j]) == 'n\'t'):
								new_s = new_s
							elif (str(doc[j]) == 'ca') and (str(doc[j+1]) == 'n\'t'):
								new_s = new_s + ' can'
							elif (str(doc[j]) == 'wo') and (str(doc[j+1]) == 'n\'t'):
								new_s = new_s + ' will'
							else:
								new_s = new_s + ' ' + w



							#j += 1

						# if j == first_subj - 1:
						# 	new_s = new_s + w + ' not '
						# else:
						# 	new_s = new_s + w + ' '
						j += 1

				else:
					new_s = s
			else:
				new_s = s

			new_s = new_s.lstrip()
			new_sentences = new_sentences + "\"" + new_s + "\"" + '\n'
		# eliminate the last space using rstrip()
		new_sentences = new_sentences.rstrip()
		# print(sentences[i])
		# print()
		# print()
		print(new_sentences)
		# if sentences[i] == new_sentences:
		# 	print(new_sentences)
		# 	print()
		# 	print('No antonymy was applied, index ', i)
		# 	print(sentences[i])
		# all_sentences.append(new_sentences)


	# final = pd.DataFrame({
	# 	'Antonymy sentences': all_sentences,
	# 	'Labels': np.nan
	# 	})
	# final.to_csv('../antonymy5000.csv', encoding='utf-8')

	


				

		


			