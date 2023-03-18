

import numpy as np # linear algebra
import time
import cv2
import glob
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import shutil
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image





img_dir = 'C:/Users/LONG KHANH/Downloads/AI CLUB/me/images'


num_images = len(glob.glob(os.path.join(img_dir , "*.jpg")))
print("Number of images:", num_images)

# Set the path to the directory containing the images


# Get a list of all image file names in the directory
img_files = [file for file in os.listdir(img_dir) if file.endswith('.jpg')]
# Create an empty list to store the image sizes
img_sizes = []


# Iterate over each image file in the directory
for file in img_files:
    # Open the image and get its size
    with Image.open(os.path.join(img_dir, file)) as img:
        size = img.size
    # Add the image size to the list
    img_sizes.append(size)


width =[t[0] for t in img_sizes]
height =[t[1] for t in img_sizes]

print(img_sizes)

#Scatter plot: width vs height
plt.scatter(width, height)
plt.xlabel('width')
plt.ylabel('height')

# Set the plot title
plt.title('Scatter plot between width and height')

# Show the plot
plt.show()



## Height distribution
sns.histplot(height, binwidth  = 10)

plt.xlabel('height')
plt.ylabel('count')
plt.title('Distribution of heights')

# Display the plot
plt.show()





## Width distribution
sns.histplot(width, binwidth  = 10)

plt.xlabel('width')
plt.ylabel('count')
plt.title('Distribution of widths')

# Display the plot
plt.show()


#ratio distribution
ratio = [a / b for a, b in zip(width, height)]
sns.histplot(ratio, bins=100)
# Set the axis labels and title
plt.xlabel('Ratio of Width to Height')
plt.ylabel('Count')
plt.title('Ratio Distribution Histogram')

# Display the plot
plt.show()



#disorder size distribution histogram
df_test = pd.DataFrame({'Shapes': img_sizes})
test_counts = df_test['Shapes'].value_counts()
test_counts_sorted = test_counts.sort_index()

# Create a bar plot of the image size counts
ax = test_counts_sorted.plot(kind='bar')

# Set the axis labels and title
ax.set_xlabel('Image Size')
ax.set_ylabel('Count')
ax.set_title('Size Distribution Histogram disorder')


# Display the plot
plt.show()




#desceding size distribution histogram
test_counts_sorted = test_counts.sort_values(ascending = False)
# Create a bar plot of the image size counts
ax = test_counts_sorted.plot(kind='bar')

# Set the axis labels and title
ax.set_xlabel('Image Size')
ax.set_ylabel('Count')
ax.set_title('Desceding Size Distribution Histogram')

# Display the plot
plt.show()










