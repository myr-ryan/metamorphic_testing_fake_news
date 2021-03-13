# coding=utf-8
import numpy as np
import pandas as pd
import random
from functions import *


def MR_5(browser):
	metamorphic_testing(browser, '../reason_lists.csv', '../shuffle.csv')

	# shuffled_sentences = []

	# for i in range(len(sentences)):
	# 	print('Processing index ', i)
	# 	sentence = sentences[i].split('\n')
	# 	random.shuffle(sentence)
	# 	new_sentences = '\n'.join(sentence)
	# 	shuffled_sentences.append(new_sentences)


	# final = pd.DataFrame({
	# 	'Shuffled sentences': shuffled_sentences,
	# 	'Labels': np.nan
	# 	})
	# final.to_csv('../shuffle.csv', encoding='utf-8')
