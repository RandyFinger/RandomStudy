# This is an ongoing study to research the behavior of  python's native random library. 

import pandas as pd
import numpy as np
import matplotlib as plot
import random

# Generate an array of random values. 1d array size = 10 
a = np.zeros((10), dtype=np.int16)

# iterate through array and assign random values between 1 and 10
i = 0
while i < a.size:
    a[i] = random.randint(1, 10)
    i += 1

# Print array a
print(a)