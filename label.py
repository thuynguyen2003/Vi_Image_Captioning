import pandas as pd
import csv
import json
import re
import numpy as np
from collections import Counter
import  collections
from matplotlib import pyplot as plt

newline_char = '\n'
tsv_data = []
filename = "C:/Users/LONG KHANH/Downloads/AI CLUB/UIT-ViIC/UIT-ViIC/oscar_format/test.label.tsv"






with open(filename, "r", encoding= "UTF-8") as tsvfile:
    for row in tsvfile:
        # remove new-line charater -
        row = row.strip(newline_char)
        # separate the cells on comma (csv file)
        cells = row.split(",")  # split the line into cells
        tsv_data.append(cells)

my=[]

for row in tsv_data:
        state = row[0]
        my_list = state.split("\t")
        for i in range ( 1, len(my_list), 6):
            word = my_list[i].split(":")[-1].strip().strip("'")
            my.append(word)


new_list = list(filter(lambda x: x.strip() != "", my))




## SCATTER PLOT BETWEEN LENGTH VS FREQUENCY
freq_dict = {}
for s in new_list:
    length = len(s)
    if length in freq_dict:
        freq_dict[length] += 1
    else:
        freq_dict[length] = 1

# Create lists of length and frequency
lengths = []
frequencies = []
for length, frequency in freq_dict.items():
    lengths.append(length)
    frequencies.append(frequency)

# Create scatter plot
plt.scatter(lengths, frequencies)
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.title('WORD Length vs Frequency')
plt.show()







#TOP 10 COMMON WORD IN HISTOGRAM

word_counts = collections.Counter(new_list)

# get the top 10 most common words
top_words = word_counts.most_common(10)

# extract the words and counts into separate lists
word_labels = [word[0] for word in top_words]
word_counts = [word[1] for word in top_words]

# create the bar chart
plt.bar(word_labels, word_counts)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words')
plt.show()












#TEXT DISTRIBUTION ( MIN = 100)

unique_labels, label_counts = np.unique(new_list, return_counts=True)

element_counts = Counter(new_list)

# filter unique elements by occurrence count
min_count = 100
filtered_counts = {element: count for element, count in element_counts.items() if count >= min_count}

# separate elements and counts into separate lists
filtered_elements = list(filtered_counts.keys())
filtered_counts = list(filtered_counts.values())

# create bar chart
plt.bar(filtered_elements, filtered_counts)

# set title and axis labels
plt.title('Class Distribution (min count = {})'.format(min_count))
plt.xlabel('Class')
plt.ylabel('Count')

# show plot
plt.show()









