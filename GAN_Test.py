import numpy as np
import random
import os
from glob import glob
import cv2
import matplotlib.pyplot as plt
from PIL import Image

DATADIR = "C:\\Users\\jun17\\PycharmProjects\\GAN\\GPS_data\\Train\\"
CATEGORIES =["Discrim","Generator"]

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

print(len(training_data))
random.shuffle(training_data)

for sample in training_data:
    print(sample[1])

X = []
Y = []

for features, label in training_data:
    X.append(features)
    Y.append(label)

x = np.array(X).reshape(-1, 256, 256, 1)

import pickle

pickle_out = open("x.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

print(X[1])