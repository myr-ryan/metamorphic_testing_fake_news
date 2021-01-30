# coding=utf-8
from selenium import webdriver
import selenium
import time
import pandas as pd 
from read_file import *
from is_safe_url import *
from MR_4 import *
from MR_5 import *
from MR_6 import *
import numpy as np

# # use chrome driver
# path = '/Users/mayingrui/Desktop/FYP/Dataset/chromedriver'
# browser = webdriver.Chrome(executable_path=path)


# enter text
#text = 'https://indianexpress.com/article/sports/sport-others/snooker-legend-willie-thorne-passes-away-6463688/'
#text = ['https://www.bbc.com/news/explainers-53517968', 'https://www.thesun.co.uk/news/13706467/pilot-indonesia-plane-looked-dishevelled/', 'https://www.thesun.co.uk/news/13706034/beast-from-the-east-snow-5c-daytime-temperatures/', 'https://www.thesun.co.uk/news/13701086/meghan-markle-prince-harry-invited-queen-trooping-the-colour/', 'https://www.thesun.co.uk/news/13705895/hospitals-shared-by-coronavirus-sceptics/']
#check_safety('../gossipcop_fake.csv')

check_safety('../gossipcop_real.csv')
#直接运行就好

#check_safety('../politifact_fake.csv')
#check_safety('../politifact_real.csv')
#read_csv('../gossipcop_fake.csv')
#joint_files('../workable_url.csv', '../workable_url1.csv')
#joint_files('../safe_url.csv', '../safe_url1.csv')

# ##########
# text_in_df = pd.read_csv('../workable_url.csv')
# sentences_with_label = pd.read_csv('../reason_lists1.csv', encoding='utf-8')

# #0:500
# text = text_in_df[text_in_df.columns[1]].values.tolist()[0:500]
# sentences = sentences_with_label[sentences_with_label.columns[1]].values.tolist()
# labels = sentences_with_label[sentences_with_label.columns[2]].values.tolist()


#MR-4: Consistence with Reason List
#MR_4(browser, text)

#MR-5 Permutation of Words
#MR_5(browser, sentences, labels)

#MR-6 Shuffle of Sentences
#MR_6(browser, sentences, labels)
#print(len(sentences))

##########

# # #screenshot of the page
# # browser.save_screenshot('blablabla.png')





