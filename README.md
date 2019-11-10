# MakeMyOwnDataset
Explanation for making my own dataset for tensorflow


Import
---------------
<pre><code>
import numpy as np
import random 
import os
import cv2
import matplotlib.pyplot as plt
</code></pre>

Lib 'random' is imported for shuffling, and lib 'os' is used for reaching to the Directory.


Directory setting
----------------
<pre><code>
DATADIR = "C:\\Users\\jun17\\PycharmProjects\\GAN\\GPS_data\\Train\\"
CATEGORIES =["Discrim","Generator"]
</code></pre>

DATADIR is the directory to File name "Discrim","Generator".

CATEGORIES has the categories that this code has to handle. (later used as Label)

Create training data
-----------------
<pre><code>
training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                training_data.append([img_array, class_num])
            except Exception as e:
                pass

create_training_data()
</code></pre>

Variable 'path' has the directory to 2 files, "Discriminator","Generator". 

Inside the second for loop, variable img_array has and option cv2.IMREAD_GRAYSCALE. 

This makes all the images as a shape as (256,256,1) ==> single channel image. 
