import numpy as np
import matplotlib.pyplot as plt
import csv

# sample data
x = []
y = []

with open('women_marathon.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		x.append(float(row[0]))
		#transfer time to minutes
		y.append(sum(i*j for i, j in zip(map(float, row[3].split(':')), [60, 1, 1/60])))

print(y)
# fit with np.polyfit
m, b = np.polyfit(x, y, 1)
print(m)
print(b)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-')