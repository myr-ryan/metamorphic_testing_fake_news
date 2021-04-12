import re
import pandas as pd
import numpy as np
import selenium
import time

def filter_emoji(desstr,restr=''):     
    try:  
        res= re.compile(u'[\U00010000-\U0010ffff]')  
    except re.error:  
        res = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')  
    return res.sub(restr, desstr)

def print_label(output):

	labels = []
	for i in range(int(len(output.splitlines()) / 2)):
		labels.append(output.splitlines()[2 * i])

	labels = sorted(labels)

	return labels

# This function will be used in MR_1, MR_2, MR_5
# The relation of the outputs will be changed according to each metamorphic relation
def metamorphic_testing(browser, file1, file2):
	url = 'https://www.fakerfact.org/'
	url_try = 'https://www.fakerfact.org/try-it-out'

	source = pd.read_csv(file1, encoding='utf-8')
	followup = pd.read_csv(file2, encoding='utf-8')

	source_sentences = source[source.columns[1]].values.tolist()[200:500]
	followup_sentences = followup[followup.columns[1]].values.tolist()[200:500]

	old_sentences = []
	source_labels = []

	new_sentences = []
	followup_labels = []

	consistence = 0
	total = len(followup_sentences)
	index = 0

	# go to fakerfact website
	browser.get(url_try)


	for i in range(len(followup_sentences)):
		print(source_sentences[i])
		print()
		print()
		print(followup_sentences[i])
		print()
		print()
		index += 1
		if type(followup_sentences[i]) != str:
			total -= 1
			print('Empty follow up sentence')
		else:

			try:
				# enter the sentences (as input)
				time.sleep(2)
				input_box = browser.find_element_by_class_name('form-control')
				input_box.send_keys(source_sentences[i])
				input_box.submit()

				# get the output
				time.sleep(4)
				output_s = print_label(browser.find_element_by_class_name('ff-flag').text)				

				# go back to 'try-it-out' page
				time.sleep(2)
				browser.get(url_try)

				time.sleep(2)
				input_box = browser.find_element_by_class_name('form-control')
				input_box.send_keys(followup_sentences[i])
				input_box.submit()

				# get the output
				time.sleep(4)
				output_f = print_label(browser.find_element_by_class_name('ff-flag').text)				

				print('Number ', index)
				print('Source test case: ', output_s)
				print('Follow-up test case: ', output_f)

				# For MR_1 and MR_5, the results should the same
				# For MR_2, the results should be different 
				if str(output_s) == str(output_f):
					consistence += 1
					print('The result correpsonds with the MR')
				else:
					print('The result does not correspond with the MR')
				print('----------')
				old_sentences.append(source_sentences[i])
				new_sentences.append(followup_sentences[i])
				source_labels.append(output_s)
				followup_labels.append(output_f)
				# go back to 'try-it-out' page
				time.sleep(2)
				browser.get(url_try)

			except selenium.common.exceptions.NoSuchElementException:
				print('**Something goes wrong**')
				total -= 1
				time.sleep(2)
				browser.get(url_try)

	rate = consistence / total
	print('The total pass rate is ', rate)
	print('Correct number is ', consistence)
	print('Total number is ', total)


	# The file names should be changed according to each metamorphic relation
	reason_file = pd.DataFrame({
		'Reason Lists': old_sentences,
		'Labels': source_labels
		})
	reason_file.to_csv('../hmr_2_old_200_500.csv', encoding='utf-8')

	reason_file = pd.DataFrame({
		'Reason Lists': new_sentences,
		'Labels': followup_labels
		})
	reason_file.to_csv('../hmr_2_new_200_500.csv', encoding='utf-8')













