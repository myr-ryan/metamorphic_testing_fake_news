# coding=utf-8
from selenium import webdriver
import selenium
import time
import pandas as pd 
from read_file import *
from is_safe_url import *
#from MR_1 import *
from MR_2 import *
#from MR_3 import *
#from MR_4 import *
#from MR_5 import *
import numpy as np

# # use chrome driver
# path = '/Users/mayingrui/Desktop/FYP/Dataset/chromedriver'
# browser = webdriver.Chrome(executable_path=path)

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



##########
#text_in_df = pd.read_csv('../workable_url.csv')

#从这一行开始
sentences_with_label = pd.read_csv('../reason_lists.csv', encoding='utf-8')

# #0:500
# #text = text_in_df[text_in_df.columns[1]].values.tolist()[19500:]


sentences = sentences_with_label[sentences_with_label.columns[1]].values.tolist()[3:4]
labels = sentences_with_label[sentences_with_label.columns[2]].values.tolist()[3:4]


# #MR-1: Consistence with Synonymy
# #MR_1(browser, sentences, labels)
#MR_1(browser)
# ##到这一行结束

#MR-2: Opposite Results after Antonymy
# 运行完0-200了
MR_2(sentences, labels)



#MR-3: Consistence with Reason List
#MR_3(browser, text)

#MR-4 Permutation of Words
#MR_4(browser, sentences, labels)

# MR-5 Shuffle of Sentences
#MR_5(browser)


# ##########


# # #screenshot of the page
# # browser.save_screenshot('blablabla.png')





