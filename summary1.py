import numpy as np

data = [10, 20, 30, 40, 50, 60, 70, 80]

summary = np.percentile(
    data,
    [0, 25, 50, 75, 100]
)

print(summary)