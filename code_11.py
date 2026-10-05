import numpy as np
import pandas as pd

# Set the seed so the random numbers are the same every time you run it
np.random.seed(42)

# Generate 10 random whole numbers from 1 to 100
data = np.random.randint(1, 101, 10)

# Convert the array of random numbers into a Pandas Series
s = pd.Series(data)

print(s)