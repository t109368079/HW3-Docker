# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:43:45 2024

@author: Yuuki
"""

import os
import socket

def count_words(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    total_words = 0
    for line in lines:
        words = line.split(' ')
        total_words += len(words)
    
    return total_words

writed_string = ""
#%% 1. List name of all the text file at /home/data

folder_path = '/home/data'
files = os.listdir(folder_path)
files = [file for file in files if file.endswith('.txt')]

str_ = "Folder /home/data/ contains: "
print(str_)
writed_string += str_+'\n'
for file in files:
    str_ = f"{file}"
    writed_string += str_+'\n'
    print(str_)

#%% Read two text files and count total number of words
writed_string += '\n'
words_in_folder = 0
for file in files:
    total_words = count_words(os.path.join(folder_path,file))
    words_in_folder += total_words
    
    str_ = f'Number of words in {file}: {total_words}'
    writed_string += str_ + '\n'
    print(str_)

str_ = f'Total words in /data folder : {words_in_folder}' 
writed_string += str_ + '\n'
print(str_)
#%% List the top 3 words with maximum number of count in IF.txt
writed_string += '\n'
with open('/home/data/IF.txt', 'r') as f:
    lines = f.readlines()

word_dict = {}
for line in lines:
    words = line.split(' ')
    
    for word in words:
        if word not in list(word_dict.keys()):
            word_dict.update({word:1})
        else:
            word_dict[word] += 1

sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
for i, item in enumerate(sorted_dict[:3]):
    str_ = f'Top {i+1} word: "{item[0]}", number of count: {item[1]}' 
    writed_string += str_ + '\n'
    print(str_)
    
#%% Find the IP address of my machine
writed_string += '\n'
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

str_ = f"IP address is : {ip_address}"
writed_string += str_ + '\n'
print(str_)

#%% Write result to txt file

with open('/home/output/result.txt', 'w') as f:
    f.write(writed_string)

