# coding=utf-8
from functions import *
import numpy as np
import pandas as pd
import time


def HMR_1(browser):
	# all_sentences = []
	# for i in range(len(sentences)):
	# 	sentence = sentences[i].split('\n')
	# 	new_sentences = ''
	# 	for s in sentence:
	# 		s = s[1:-1]
	# 		new_sentences = new_sentences + s + '\n'
		
	# 	all_sentences.append(new_sentences)


	# final = pd.DataFrame({
	# 	'Sentences without quotation marks': all_sentences,
	# 	'Labels': np.nan
	# 	})
	# final.to_csv('../HMR_1.csv', encoding='utf-8')

	metamorphic_testing(browser, '../reason_lists.csv', '../HMR_1.csv')