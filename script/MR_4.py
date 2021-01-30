# coding=utf-8
import time
import selenium
from functions import *
import pandas as pd 

url = 'https://www.fakerfact.org/'
url_try = 'https://www.fakerfact.org/try-it-out'

def MR_4(browser, text):
	# go to fakerfact website
	browser.get(url)

	correct = 0
	total = len(text)
	reasons = []
	labels = []

	for t in text:
		try:
			# find the text area, and send inputs
			time.sleep(2)
			input_box = browser.find_element_by_class_name('form-control')
			input_box.send_keys(t)
			input_box.submit()

			# find the corresponding output
			time.sleep(3)
			output = browser.find_element_by_class_name('ff-flag').text
			# click 'show more'
			time.sleep(2)
			browser.find_element_by_xpath("//a[@href='#less']").click()

			# find the reason list
			time.sleep(2)
			reason_list = browser.find_element_by_class_name('ff-copy').text
			reason_list = filter_emoji(reason_list)

			# go to 'try it out' page
			time.sleep(2)
			browser.get(url_try)


			# enter the reason list (as input)
			time.sleep(2)
			input_box = browser.find_element_by_class_name('form-control')
			input_box.send_keys(reason_list)
			input_box.submit()

			# get the output again
			time.sleep(4)
			output_new = browser.find_element_by_class_name('ff-flag').text

			first = print_label(output)
			second = print_label(output_new)
			print('Source Test case result: ', first)
			print('Follow-up Test case result:', second)
			if set(second) <= set(first):
				print('The result correpsonds with the MR')
				correct += 1
			else:
				print('The result does not correspond with the MR')
			reasons.append(reason_list)
			labels.append(second)
			print('-----------------------------------')

			# go back to 'url' page
			time.sleep(2)
			browser.get(url)
			#print(output)

		except selenium.common.exceptions.NoSuchElementException:
			print('**Less than 100 words! or no reason list**')
			total -= 1
			time.sleep(2)
			browser.get(url)

	rate = correct / total
	print('The total pass rate is ', rate)
	print('Correct number is ', correct)
	print('Total number is ', total)
	reason_file = pd.DataFrame({
		'Reason Lists': reasons,
		'Labels': labels
		})
	reason_file.to_csv('../reason_lists1.csv', encoding='utf-8')
