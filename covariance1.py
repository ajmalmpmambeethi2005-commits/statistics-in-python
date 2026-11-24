import numpy as np

study_hours = [1, 2, 3, 4]
marks = [20, 30, 40, 50]

covariance_matrix = np.cov(study_hours, marks)

print(covariance_matrix)

print("Sample covariance:", covariance_matrix[0, 1])