# coding=utf-8
from selenium import webdriver
import selenium
import time
import pandas as pd 
from read_file import *
from is_safe_url import *
#from MR_1 import *
#from MR_2 import *
#from MR_3 import *
#from MR_4 import *
#from MR_5 import *
#from HMR_1 import *
from HMR_2 import *
import numpy as np

# use chrome driver
path = '/Users/mayingrui/Desktop/FYP/Dataset/chromedriver'
browser = webdriver.Chrome(executable_path=path)

# # check url safety by running the four lines below
# check_safety('../gossipcop_fake.csv')
# check_safety('../gossipcop_real.csv')
# check_safety('../politifact_fake.csv')
# check_safety('../politifact_real.csv')

# check whether the url is still workable or not
#read_csv('../safe_url.csv')


# # joint different csv files, for the purpose of generating workable url and safe url
#joint_files_workable('../workable_url.csv', '../workable_url1.csv')
#joint_files_safe('../safe_url.csv', '../safe_url1.csv')
#joint_files_reason_lists('../antonymy.csv', '../antonymy5000.csv')


#text_in_df = pd.read_csv('../workable_url.csv')


# sentences_with_label = pd.read_csv('../reason_lists.csv', encoding='utf-8')


# # #text = text_in_df[text_in_df.columns[1]].values.tolist()[19500:]


# sentences = sentences_with_label[sentences_with_label.columns[1]].values.tolist()[0:500]
# labels = sentences_with_label[sentences_with_label.columns[2]].values.tolist()


# #MR-1: Consistence with Synonymy
# #MR_1(browser, sentences, labels)
#MR_1(browser)


#MR-2: Opposite Results after Antonymy
#MR_2(browser)



#MR-3: Consistence with Reason List
#MR_3(browser, text)

#MR-4 Permutation of Words
#MR_4(browser, sentences, labels)

# MR-5 Shuffle of Sentences
#MR_5(browser)


#HMR-1 Consistence with Quotation Marks
#HMR_1(sentences)
#HMR_1(browser)


#HMR-1 Consistence with Separation Lines
#HMR_2(sentences)
HMR_2(browser)









