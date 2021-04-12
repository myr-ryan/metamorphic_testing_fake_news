# coding=utf-8
from functions import *
import numpy as np
import pandas as pd
import time

def HMR_2(browser):
	# #print(sentences)
	# all_sentences = []
	# for i in range(len(sentences)):
	# 	sentence = sentences[i].split('\n')
	# 	new_sentences = ''
	# 	for s in sentence:
	# 		new_sentences = new_sentences + s + ""
		
	# 	all_sentences.append(new_sentences)

	# #print(new_sentences)
	# final = pd.DataFrame({
	# 	'Sentences without separation lines': all_sentences,
	# 	'Labels': np.nan
	# 	})
	# final.to_csv('../HMR_2.csv', encoding='utf-8')

	metamorphic_testing(browser, '../reason_lists.csv', '../HMR_2.csv')