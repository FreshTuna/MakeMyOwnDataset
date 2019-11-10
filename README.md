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


