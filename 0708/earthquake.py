import csv
import matplotlib.pyplot as plt
import numpy as np

with open('all_month.csv', encoding='utf-8') as csvfile:  # 或者：errors='ignore'
    reader = csv.DictReader(csvfile)
    depth, mags = [], []
    for row in reader:
        row['depth'].strip()
        if len(row['depth']) == 0:
            row['depth'] = '0'
        depth.append((float(row['depth'])))
        row['mag'].strip()
        if len(row['mag']) == 0:
            row['mag'] = '0'
        mags.append((float(row['mag'])))


font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 9,
         }
font2 = {'family': 'Times New Roman',
         'style': 'italic',
         'weight': 'black',
         'size': 10,
         }
plt.figure(figsize=(12, 6))

plt.subplot(221)
plt.hist(np.array(depth), bins=500)
plt.xlabel('depth', font1)
plt.ylabel('frequency', font1)
plt.title('Frequency Histogram of focal depth', font2)

plt.subplot(222)
plt.hist(np.array(mags), bins=100, color='c')
plt.xlabel('mag', font1)
plt.ylabel('frequency', font1)
plt.title('Frequency Histogram of magnitude', font2)

plt.subplot(212)
plt.scatter(np.array(depth), np.array(mags), s=5, c='g')
plt.xlabel('depth', font1)
plt.ylabel('mag', font1)
plt.title('Scatter Diagram of depth and mag', font2)

plt.show()
